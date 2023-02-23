from invenio_records_resources.services import (
    RecordLink,
    RecordServiceConfig,
    pagination_links,
)
from invenio_records_resources.services.records.components import DataComponent
from referrer.records.api import ReferrerRecord
from referrer.services.records.permissions import ReferrerPermissionPolicy
from referrer.services.records.schema import ReferrerSchema
from referrer.services.records.search import ReferrerSearchOptions


class ReferrerServiceConfig(RecordServiceConfig):
    """ReferrerRecord service config."""

    url_prefix = "/referrer/"

    permission_policy_cls = ReferrerPermissionPolicy

    schema = ReferrerSchema

    search = ReferrerSearchOptions

    record_cls = ReferrerRecord
    # todo should i leave this here?
    service_id = "referrer"

    components = [*RecordServiceConfig.components, DataComponent]

    model = "referrer"

    @property
    def links_item(self):
        return {
            "self": RecordLink("{self.url_prefix}{id}"),
        }

    @property
    def links_search(self):
        return pagination_links("{self.url_prefix}{?args*}")
