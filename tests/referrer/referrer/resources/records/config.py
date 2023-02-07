import importlib_metadata
from invenio_records_resources.resources import RecordResourceConfig


class ReferrerResourceConfig(RecordResourceConfig):
    """ReferrerRecord resource config."""

    blueprint_name = "Referrer"
    url_prefix = "/referrer/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.referrer.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {**super().response_handlers, **entrypoint_response_handlers}
