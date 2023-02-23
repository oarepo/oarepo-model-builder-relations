from invenio_records_resources.services import (
    RecordLink,
    RecordServiceConfig,
    pagination_links,
)
from invenio_records_resources.services.records.components import DataComponent
from referred.records.api import ReferredRecord
from referred.services.records.permissions import ReferredPermissionPolicy
from referred.services.records.schema import ReferredSchema
from referred.services.records.search import ReferredSearchOptions


class ReferredServiceConfig(RecordServiceConfig):
    """ReferredRecord service config."""

    url_prefix = "/referred/"

    permission_policy_cls = ReferredPermissionPolicy

    schema = ReferredSchema

    search = ReferredSearchOptions

    record_cls = ReferredRecord
    # todo should i leave this here?
    service_id = "referred"

    components = [*RecordServiceConfig.components, DataComponent]

    model = "referred"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{self.url_prefix}{id}"),
        }

    @property
    def links_search(self):
        return pagination_links("{self.url_prefix}{?args*}")
