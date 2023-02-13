from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


def _(x):
    """Identity function for string extraction."""
    return x


class ReferrerSearchOptions(InvenioSearchOptions):
    """ReferrerRecord search options."""

    facets = {
        "metadata_invenio-ref_id": facets.metadata_invenio_ref_id,
        "metadata_invenio-ref_@v": facets.metadata_invenio_ref__version,
        "metadata_invenio-array_id": facets.metadata_invenio_array_id,
        "metadata_invenio-array_@v": facets.metadata_invenio_array__version,
        "metadata_invenio-array": facets.metadata_invenio_array,
        "metadata_invenio-nested_ref_id": facets.metadata_invenio_nested_ref_id,
        "metadata_invenio-nested_ref_@v": facets.metadata_invenio_nested_ref__version,
        "metadata_invenio-nested": facets.metadata_invenio_nested,
        "metadata_invenio-array-nested_ref-arr_id": facets.metadata_invenio_array_nested_ref_arr_id,
        "metadata_invenio-array-nested_ref-arr_@v": facets.metadata_invenio_array_nested_ref_arr__version,
        "metadata_invenio-array-nested_ref-arr": facets.metadata_invenio_array_nested_ref_arr,
        "metadata_invenio-array-nested": facets.metadata_invenio_array_nested,
        "metadata_ref_id": facets.metadata_ref_id,
        "metadata_ref_@v": facets.metadata_ref__version,
        "metadata_array_id": facets.metadata_array_id,
        "metadata_array_@v": facets.metadata_array__version,
        "metadata_array": facets.metadata_array,
        "metadata_nested_ref_id": facets.metadata_nested_ref_id,
        "metadata_nested_ref_@v": facets.metadata_nested_ref__version,
        "metadata_nested": facets.metadata_nested,
        "metadata_array-nested_ref-arr_id": facets.metadata_array_nested_ref_arr_id,
        "metadata_array-nested_ref-arr_@v": facets.metadata_array_nested_ref_arr__version,
        "metadata_array-nested_ref-arr": facets.metadata_array_nested_ref_arr,
        "metadata_array-nested": facets.metadata_array_nested,
        "_id": facets._id,
        "created": facets.created,
        "updated": facets.updated,
        "_schema": facets._schema,
    }
    sort_options = {
        **InvenioSearchOptions.sort_options,
    }
