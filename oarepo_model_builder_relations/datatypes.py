import copy

import marshmallow as ma
from marshmallow import fields
from oarepo_model_builder.datatypes import ObjectDataType
from oarepo_model_builder.entrypoints import load_model_from_entrypoint
from oarepo_model_builder.stack import ReplaceElement
from oarepo_model_builder.utils.jinja import split_base_name
from oarepo_model_builder.validation import InvalidModelException


class RelationSchema(ma.Schema):
    class RelationClassesSchema(ma.Schema):
        list = fields.String(required=False)
        nested = fields.String(required=False)
        single = fields.String(required=False)

    class ImportSchema(ma.Schema):
        import_str = fields.String(data_key="import", required=True)
        alias = fields.String(required=False)

    name = fields.String(required=False)
    model = fields.String(required=True)
    keys_field = fields.List(fields.String(), data_key="keys", required=False)
    model_class = fields.String(data_key="model-class", required=False)
    schema_prefix = fields.String(data_key="schema-prefix", required=False)
    relation_classes = fields.Nested(
        RelationClassesSchema, data_key="relation-classes", required=False
    )
    relation_class = fields.String(data_key="relation-class", required=False)
    pid_field = fields.String(data_key="pid-field", required=False)
    # TODO: relation-args
    imports = fields.List(fields.Nested(ImportSchema), required=False)

    class Meta:
        unknown = ma.RAISE


class RelationDataType(ObjectDataType):
    model_type = "relation"

    def model_schema(self, **extras):
        model = super().model_schema(**extras) or {}

        data = copy.deepcopy(self.definition)

        name = data.pop("name", self.key)
        model_name = data.pop("model")
        keys = data.pop("keys", ["id", "metadata.title"])
        model_class = data.pop("model-class", None)
        schema_prefix = data.pop("schema-prefix", self.key.title())
        base_relation_classes = {
            "list": "MetadataPIDListRelation",
            "nested": "MetadataPIDNestedListRelation",
            "single": "MetadataPIDRelation",
        }
        relation_classes = {
            **base_relation_classes,
            **data.pop("relation-classes", {}),
        }
        relation_class = data.pop("relation-class", None)
        relation_args = data.pop("relation-args", {})
        imports = data.pop("imports", [])
        pid_field = data.pop("pid-field", None)

        # import oarepo classes but only if used
        for rc_type, rc in base_relation_classes.items():
            if relation_classes[rc_type] == rc:
                imports.append({"import": rc})

        try:
            model_data = self.schema._load(model_name)
        except Exception as e:
            raise InvalidModelException("Can not load included model") from e

        model_properties = model_data["model"]["properties"]

        if not model_class:
            model_class = split_base_name(model_data["model"]["record-class"])
            imports.append({"import": model_data["model"]["record-class"]})
        if not pid_field:
            pid_field = f"{model_class}.pid"

        # insert properties
        props = {}
        for fld in keys:
            self._copy_field_definition(props, model_properties, fld, model_name)
        props["@v"] = {"type": "keyword", "marshmallow": {"field-name": "_version"}}

        self._prefix_marshmallow_classes(props, schema_prefix)

        model["type"] = "object"
        model["properties"] = props

        relation_extension = model.setdefault("relation", {})
        relation_extension["name"] = name
        relation_extension["model"] = model_name
        relation_extension["keys"] = keys
        relation_extension["model-class"] = model_class
        relation_extension["schema-prefix"] = schema_prefix
        relation_extension["relation-classes"] = relation_classes
        relation_extension["relation-class"] = relation_class
        relation_extension["relation-args"] = relation_args
        relation_extension["imports"] = imports
        relation_extension["pid-field"] = pid_field

        raise ReplaceElement({self.key: model})

    def _copy_field_definition(self, props, included_props, fld, model_name):
        field_path = fld.split(".")
        for parent in field_path[:-1]:
            if parent not in included_props:
                raise InvalidModelException(
                    f"Field path {field_path} is invalid within model {model_name}"
                )
            parent_marshmallow = copy.deepcopy(
                included_props[parent].get("marshmallow", {})
            )
            included_props = included_props[parent]["properties"]
            if parent not in props:
                props[parent] = {
                    "type": "object",
                    "properties": {},
                    "marshmallow": parent_marshmallow,
                }
                self._make_field_serializable(parent_marshmallow)
            props = props[parent]["properties"]
        if field_path[-1] in included_props:
            included_model = copy.deepcopy(included_props[field_path[-1]])
            self._make_field_serializable(included_model.get("marshmallow", None))
            props[field_path[-1]] = included_model

    def _make_field_serializable(self, marshmallow):
        if not marshmallow:
            return
        marshmallow.pop("read", None)
        marshmallow.pop("write", None)

    def _prefix_marshmallow_classes(self, props, schema_prefix):
        if not isinstance(props, dict):
            return
        if "properties" in props and isinstance(props["properties"], dict):
            # i am an object or nested
            if "marshmallow" in props:
                schema_class = props["marshmallow"].get("schema-class", None)
                if schema_class:
                    schema_class = schema_class.rsplit(".", maxsplit=1)[-1]
                    props["marshmallow"]["schema-class"] = schema_prefix + schema_class
        for v in props.values():
            self._prefix_marshmallow_classes(v, schema_prefix)

    class ModelSchema(RelationSchema, ObjectDataType.ModelSchema):
        relation = fields.Nested(RelationSchema, required=False)


DATATYPES = [RelationDataType]