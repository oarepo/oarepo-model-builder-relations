from typing import Any, List

import marshmallow as ma
from marshmallow import fields
from oarepo_model_builder.datatypes.containers.object import FieldSchema, ObjectDataType
from oarepo_model_builder.validation.utils import ImportSchema

# model.setdefault("record-service-config-components", []).append(
#     "oarepo_runtime.relations.components.CachingRelationsComponent"
# )


class StringOrSchema(fields.Field):
    def __init__(self, string_field, schema_field, **kwargs) -> None:
        super().__init__(**kwargs)
        self.string_field = string_field
        self.schema_field = schema_field

    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, str):
            return self.string_field._deserialize(value, attr, data, **kwargs)
        else:
            return self.schema_field._deserialize(value, attr, data, **kwargs)

    def _serialize(self, value, attr, obj, **kwargs):
        if isinstance(value, str):
            return self.string_field._serialize(value, attr, obj, **kwargs)
        else:
            return self.schema_field._serialize(value, attr, obj, **kwargs)

    def _validate(self, value):
        if isinstance(value, str):
            return self.string_field._validate(value)
        else:
            return self.schema_field._validate(value)


class RelationLinkSchema(ma.Schema):
    class Meta:
        unknown = ma.RAISE

    class_ = fields.String(data_key="class", attribute="class", required=False)
    args = fields.Dict(
        fields.String(),
        fields.String(),
        required=False,
    )


class RelationSchema(ma.Schema):
    class KeySchema(ma.Schema):
        key = fields.String(required=True)
        model = fields.Nested(FieldSchema, required=False)
        target = fields.String(required=False)

    name = fields.String(required=False)
    model = fields.String(required=True)
    keys_field = fields.List(
        StringOrSchema(ma.fields.String(), fields.Nested(KeySchema)),
        data_key="keys", attribute="keys",
        required=False,
    )
    link = ma.fields.Nested(RelationLinkSchema)
    imports = fields.List(fields.Nested(ImportSchema), required=False)
    flatten = fields.Boolean(required=False)

    class Meta:
        unknown = ma.RAISE


class RelationDataType(ObjectDataType):
    model_type = "relation"
    flatten: bool
    model_name: str
    relation_name: str
    internal_link: bool
    keys: List[Any]

    class ModelSchema(RelationSchema, ObjectDataType.ModelSchema):
        pass

    def prepare(self, context):
        data = self.definition
        self.flatten = data.get("flatten", False)
        self.model_name = data["model"]
        self.internal_link = self.model_name.startswith("#")
        self.keys = self._transform_keys(
            data.get("keys", ["id", "metadata.title"]), self.flatten
        )
        self.relation_name = data.get("name")
        super().prepare(context)

    def _transform_keys(self, keys, flatten):
        transformed_keys = []
        for k in keys:
            if isinstance(k, str):
                k = {"key": k, "target": k}
            if not k.get("target"):
                k["target"] = k["key"]
            if flatten and k["target"].startswith("metadata."):
                k["target"] = k["target"][len("metadata.") :]
            transformed_keys.append(k)
        return transformed_keys

DATATYPES = [RelationDataType]
