from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import ConstantField
from invenio_records_resources.records.api import Record
from invenio_records_resources.records.dumpers import CustomFieldsDumperExt
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from oarepo_runtime.cf import InlinedCustomFields
from referred.records.dumper import ReferredDumper
from referred.records.models import ReferredMetadata


class ReferredRecord(Record):
    model_cls = ReferredMetadata

    schema = ConstantField("$schema", "local://referred-1.0.0.json")

    index = IndexField("referred-referred-1.0.0")

    pid = PIDField(
        create=True, provider=RecordIdProviderV2, context_cls=PIDFieldContext
    )

    dumper_extensions = [
        CustomFieldsDumperExt("TEST_CF"),
    ]
    dumper = ReferredDumper(extensions=dumper_extensions)

    inlined_custom_fields = InlinedCustomFields("TEST_CF")
