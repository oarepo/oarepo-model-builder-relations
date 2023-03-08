from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


def _(x):
    """Identity function for string extraction."""
    return x


class ReferredSearchOptions(InvenioSearchOptions):
    """ReferredRecord search options."""

    facets = {
        "metadata_hint": facets.metadata_hint,
        "metadata_price": facets.metadata_price,
        "metadata_arr": facets.metadata_arr,
        "_id": facets._id,
        "created": facets.created,
        "updated": facets.updated,
        "_schema": facets._schema,
    }
    sort_options = {
        **InvenioSearchOptions.sort_options,
    }
