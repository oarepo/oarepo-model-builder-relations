from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.dumpers.relations import RelationDumperExt
from invenio_records.systemfields import ConstantField, RelationsField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from invenio_records_resources.records.systemfields.relations import (
    PIDListRelation,
    PIDNestedListRelation,
    PIDRelation,
)
from oarepo_runtime.relations import (
    # InternalListRelation,
    # InternalNestedListRelation,
    # InternalRelation,
    MetadataPIDListRelation,
    MetadataPIDNestedListRelation,
    MetadataPIDRelation,
)
from referred.records.api import ReferredRecord
from referrer.records.dumper import ReferrerDumper
from referrer.records.models import ReferrerMetadata


from invenio_records.systemfields.relations import (
    RelationResult,
    RelationListResult,
    RelationNestedListResult,
    RelationBase,
)

from invenio_records.dictutils import dict_lookup, dict_set


class InternalResult(RelationResult):
    def _lookup_id(self):
        return (super()._lookup_id(), self.record)

    def _dereference_one(self, data, keys, attrs):
        """Dereference a single object into a dict."""

        # Get related record
        obj = self.resolve((data[self.field._value_key_suffix], self.record))
        # Inject selected key/values from related record into
        # the current record.

        # From record dictionary
        if keys is None:
            data.update({k: v for k, v in obj.items()})
        else:
            new_obj = {}
            for k in keys:
                try:
                    val = dict_lookup(obj, k)
                    if val:
                        dict_set(new_obj, k, val)
                except KeyError:
                    pass
            data.update(new_obj)

        # From record attributes (i.e. system fields)
        for a in attrs:
            data[a] = getattr(obj, a)

        return data


class InternalRelation(RelationBase):
    result_cls = InternalResult

    def __init__(self, *args, pid_field=None, **kwargs):
        """Initialize the PK relation."""
        self.pid_field = pid_field
        super().__init__(*args, **kwargs)

    def resolve(self, id_):
        pid_field = self.pid_field
        if not id_:
            return None
        field_or_array = dict_lookup(id_[1], pid_field)
        if not field_or_array:
            return None

        if isinstance(field_or_array, dict):
            field_or_array = [field_or_array]
        if not isinstance(field_or_array, list):
            raise KeyError(
                f"PID field {pid_field} does not point to an object or array of objects"
            )
        for f in field_or_array:
            if not isinstance(f, dict):
                raise KeyError(
                    f"PID field {pid_field} does not point to an array of objects - array member is {type(f)}: {f}"
                )
            if id_[0] == f.get("id", None):
                return f
        return None


class ReferrerRecord(Record):
    model_cls = ReferrerMetadata

    schema = ConstantField("$schema", "local://referrer-1.0.0.json")

    index = IndexField("referrer-referrer-1.0.0")

    pid = PIDField(
        create=True, provider=RecordIdProviderV2, context_cls=PIDFieldContext
    )

    dumper_extensions = [
        RelationDumperExt("relations"),
    ]
    dumper = ReferrerDumper(extensions=dumper_extensions)

    relations = RelationsField(
        internal_ref=InternalRelation(
            "metadata.internal-ref",
            keys=["id", "test"],
            pid_field="metadata.obj",
        ),
        internal_ref_arr=InternalRelation(
            "metadata.internal-ref-arr",
            keys=["id", "test"],
            pid_field="metadata.arr",
        ),
        internal_ref_arrobj=InternalRelation(
            "metadata.internal-ref-arrobj",
            keys=["id", "test"],
            pid_field="metadata.arrobj",
        ),
        # ref=InternalListRelation(
        #     "metadata.internal-nested",
        #     keys=["id", "test"],
        #     pid_field="metadata.arr",
        #     relation_field="ref",
        # ),
        # ref_arr_item=InternalNestedListRelation(
        #     "metadata.internal-array-nested",
        #     keys=["id", "test"],
        #     pid_field="metadata.arr",
        #     relation_field="ref-arr",
        # ),
        invenio_ref=PIDRelation(
            "metadata.invenio-ref",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
        ),
        invenio_array_item=PIDListRelation(
            "metadata.invenio-array",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
        ),
        invenio_nested=PIDListRelation(
            "metadata.invenio-nested",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
            relation_field="ref",
        ),
        ref_arr_item_1=PIDNestedListRelation(
            "metadata.invenio-array-nested",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
            relation_field="ref-arr",
        ),
        ref_1=MetadataPIDRelation(
            "metadata.ref",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
        ),
        array=MetadataPIDListRelation(
            "metadata.array",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
        ),
        nested=MetadataPIDListRelation(
            "metadata.nested",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
            relation_field="ref",
        ),
        ref_arr_item_2=MetadataPIDNestedListRelation(
            "metadata.array-nested",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
            relation_field="ref-arr",
        ),
        cf=MetadataPIDRelation(
            "metadata.cf",
            keys=["id", "metadata.title", "test"],
            pid_field=ReferredRecord.pid,
        ),
    )
