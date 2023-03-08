import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig
from referred.resources.records.ui import ReferredUIJSONSerializer


class ReferredResourceConfig(RecordResourceConfig):
    """ReferredRecord resource config."""

    blueprint_name = "Referred"
    url_prefix = "/referred/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.referred.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                ReferredUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
