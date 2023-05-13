import json

from oarepo_model_builder.datatypes import (
    DataType,
    DataTypeComponent,
    ModelDataType,
    datatypes,
)
from oarepo_model_builder.datatypes.components import DefaultsModelComponent
from oarepo_model_builder.utils.python_name import convert_name_to_python
from oarepo_model_builder.validation import InvalidModelException

from oarepo_model_builder_relations.datatypes import RelationDataType


class RelationModelComponent(DataTypeComponent):
    eligible_datatypes = [ModelDataType]
    affects = [DefaultsModelComponent]

    def after_model_prepare(self, datatype: DataType, *, context, **kwargs):
        relation_datatypes = []
        for dt in datatype.deep_iter():
            if isinstance(dt, RelationDataType):
                relation_datatypes.append(dt)

        for dt in relation_datatypes:
            datatypes.call_components(dt, "resolve_relation", context=context)
            datatypes.call_components(dt, "prepare_relation_children", context=context)

        relation_names = {}
        for dt in relation_datatypes:
            datatypes.call_components(
                dt, "get_declared_relation_names", relation_names=relation_names
            )
        for dt in relation_datatypes:
            datatypes.call_components(
                dt, "set_relation_names", relation_names=relation_names
            )


class RelationComponent(DataTypeComponent):
    eligible_datatypes = [RelationDataType]

    def resolve_relation(self, datatype: RelationDataType, *, context, **kwargs):
        if datatype.internal_link:
            root_datatype = datatype.stack[0]
            dt_id = datatype.model_name[1:]
        else:
            loaded_schema = datatype.schema._load('referred')
            root_datatype = datatypes.get_datatype(
                datatype,
                loaded_schema['model'],
                None,
                datatype.model,
                datatype.schema)
            root_datatype.prepare({
                'profile': context['profile'],
                'profile_module': context['profile_module'],
                'profile_upper': context['profile_upper'],
            })
            if '#' in datatype.model_name:
                dt_id = datatype.model_name.split('#', maxsplit=1)[1]
            else:
                dt_id = None

        if not dt_id:
            datatype.related_data_type = root_datatype
            return

        for dt in root_datatype.deep_iter():
            if dt.id == dt_id:
                datatype.related_data_type = dt
                return

        raise InvalidModelException(
            f"No element found for reference {datatype.model_name}"
        )

    def prepare_relation_children(
        self, datatype: RelationDataType, *, context, **kwargs
    ):
        # insert properties
        children = {}
        child_tree = {}
        for fld in datatype.keys:
            if fld.get("model"):
                child = datatypes.get_datatype(
                    datatype, fld["model"], fld["target"], datatype.model, datatype.schema
                )
                child.prepare({
                    'profile': context['profile'],
                    'profile_module': context['profile_module'],
                    'profile_upper': context['profile_upper'],
                })
            else:
                child = self.find_child(datatype.related_data_type, fld)
            children[child.key] = child

        children["@v"] = datatypes.get_datatype(
            datatype,
            {
                "type": "keyword",
                "marshmallow": {
                    "field-name": "_version",
                    "field-class": "ma_fields.String",
                },
                "ui": {
                    "marshmallow": {
                        "field-name": "_version",
                        "field-class": "ma_fields.String",
                    }
                },
            },
            "@v",
            datatype.model,
            datatype.schema,
        )
        children['@v'].prepare({
            'profile': context['profile'],
            'profile_module': context['profile_module'],
            'profile_upper': context['profile_upper'],
        })

        datatype.children = children

    def find_child(self, datatype, fld):
        target = fld["key"].split('.')
        dt = datatype
        for t in target:
            if not dt:
                raise InvalidModelException(
                    f"Path {target} not found in datatype "
                    f"{datatype.path}: {json.dumps(datatype.definition, indent=4)}"
                )
            while hasattr(dt, 'item'):
                dt = dt.item
            if t not in dt.children:
                raise InvalidModelException(
                    f"Path {target} not found in datatype "
                    f"{datatype.path}. "
                    f"Error at {dt.path}: {t} not found at its children. "
                    f"Datatype content:"
                    f"{json.dumps(datatype.definition, indent=4)}"
                )
            dt = dt.children[t]
        ret = dt.copy()
        ret.key = fld["target"]
        return ret

    def get_declared_relation_names(self, datatype, *, relation_names, **kwargs):
        if datatype.relation_name and datatype.relation_name not in relation_names:
            relation_names[datatype.relation_name] = datatype

    def set_relation_names(self, datatype, *, relation_names, **kwargs):
        if (
            datatype.relation_name
            and relation_names[datatype.relation_name] is datatype
        ):
            return
        # conflict found, try to resolve it
        relation_name = datatype.relation_name
        p: DataType
        for p in reversed(datatype.parent.stack):
            if p.key:
                relation_name = convert_name_to_python(f"{p.key}_{relation_name}")
                if relation_name not in relation_names:
                    # found unused name, use it
                    datatype.relation_name = relation_name
                    relation_names[relation_name] = datatype
                    return
        # could not get unused name, add _1, ... to it
        for p in range(1, 100):
            new_relation_name = f"{relation_name}_{p}"
            if new_relation_name not in relation_names:
                # found unused name, use it
                datatype.relation_name = new_relation_name
                relation_names[new_relation_name] = datatype
                return
        raise InvalidModelException(
            "Could not generate relation name for {datatype.path}: "
            'please specify "name" yourself.'
        )

COMPONENTS = [RelationComponent, RelationModelComponent]
