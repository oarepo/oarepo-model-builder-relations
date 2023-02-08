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
    MetadataPIDListRelation,
    MetadataPIDNestedListRelation,
    MetadataPIDRelation,
)
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
        RelationDumperExt("relations"),
    ]
    dumper = ReferrerDumper(extensions=dumper_extensions)

    relations = RelationsField(
        invenio_ref=PIDRelation(
            "metadata.invenio-ref",
            keys=["id", "metadata.title"],
            pid_field=ReferredRecord.pid,
        ),
        items=PIDListRelation(
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
        ref=MetadataPIDRelation(
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
    )
