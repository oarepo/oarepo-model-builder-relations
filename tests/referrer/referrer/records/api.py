from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import ConstantField, RelationsField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.dumpers import CustomFieldsDumperExt
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from oarepo_runtime.cf import InlinedCustomFields
from oarepo_runtime.relations import InternalRelation, PIDRelation, RelationsField
from referred.records.api import ReferredRecord
from referrer.records.dumper import ReferrerDumper
from referrer.records.models import ReferrerMetadata


class ReferrerRecord(Record):
    model_cls = ReferrerMetadata

    schema = ConstantField("$schema", "local://referrer-1.0.0.json")

    index = IndexField("referrer-referrer-1.0.0")

    pid = PIDField(
        create=True, provider=RecordIdProviderV2, context_cls=PIDFieldContext
    )

    dumper_extensions = [
        CustomFieldsDumperExt("TEST_CF"),
    ]
    dumper = ReferrerDumper(extensions=dumper_extensions)

    inlined_custom_fields = InlinedCustomFields("TEST_CF")

    relations = RelationsField(
        internal_ref=InternalRelation(
            "metadata.internal-ref",
            keys=["id", "test"],
            related_part="metadata.obj",
        ),
        internal_ref_arr=InternalRelation(
            "metadata.internal-ref-arr",
            keys=["id", "test"],
            related_part="metadata.arr",
        ),
        internal_ref_arrobj=InternalRelation(
            "metadata.internal-ref-arrobj",
            keys=["id", "test"],
            related_part="metadata.arrobj",
        ),
        internal_array_ref_array_item=InternalRelation(
            "metadata.internal-array-ref-array",
            keys=["id", "test"],
            related_part="metadata.arr",
        ),
        ref=InternalRelation(
            "metadata.internal-array-object-ref-array.ref",
            keys=["id", "test"],
            related_part="metadata.arr",
        ),
        ref_arr_item=InternalRelation(
            "metadata.internal-array-nested.ref-arr",
            keys=["id", "test"],
            related_part="metadata.arr",
        ),
        internal_cf=InternalRelation(
            "metadata.internal-cf",
            keys=["id", "test"],
            related_part="",
        ),
        invenio_ref=PIDRelation(
            "metadata.invenio-ref",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
        ),
        invenio_array_item=PIDRelation(
            "metadata.invenio-array",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
        ),
        invenio_nested=PIDRelation(
            "metadata.invenio-nested.ref",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
        ),
        ref_arr_item_1=PIDRelation(
            "metadata.invenio-array-nested.ref-arr",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
        ),
        ref_1=PIDRelation(
            "metadata.ref",
            keys=["id", {"key": "metadata.title", "target": "title"}],
            pid_field=ReferredRecord.pid,
        ),
        array=PIDRelation(
            "metadata.array",
            keys=["id", {"key": "metadata.title", "target": "title"}],
            pid_field=ReferredRecord.pid,
        ),
        nested=PIDRelation(
            "metadata.nested.ref",
            keys=["id", {"key": "metadata.title", "target": "title"}],
            pid_field=ReferredRecord.pid,
        ),
        ref_arr_item_2=PIDRelation(
            "metadata.array-nested.ref-arr",
            keys=["id", {"key": "metadata.title", "target": "title"}],
            pid_field=ReferredRecord.pid,
        ),
        cf=PIDRelation(
            "metadata.cf",
            keys=["id", {"key": "metadata.title", "target": "title"}, "test"],
            pid_field=ReferredRecord.pid,
        ),
    )
