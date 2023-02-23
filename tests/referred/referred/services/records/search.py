from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


def _(x):
    """Identity function for string extraction."""
    return x


class ReferredSearchOptions(InvenioSearchOptions):
    """ReferredRecord search options."""

    facets = {
        "hint": facets.hint,
        "price": facets.price,
        "arr": facets.arr,
        "_id": facets._id,
        "created": facets.created,
        "updated": facets.updated,
        "_schema": facets._schema,
    }
    sort_options = {
        **InvenioSearchOptions.sort_options,
    }
