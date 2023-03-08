from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


def _(x):
    """Identity function for string extraction."""
    return x


class ReferrerSearchOptions(InvenioSearchOptions):
    """ReferrerRecord search options."""

    facets = {
        "metadata_obj_test": facets.metadata_obj_test,
        "metadata_obj_id": facets.metadata_obj_id,
        "metadata_arr_test": facets.metadata_arr_test,
        "metadata_arr_id": facets.metadata_arr_id,
        "metadata_arrobj_test": facets.metadata_arrobj_test,
        "metadata_arrobj_id": facets.metadata_arrobj_id,
        "metadata_internal_ref_id": facets.metadata_internal_ref_id,
        "metadata_internal_ref_test": facets.metadata_internal_ref_test,
        "metadata_internal_ref__version": facets.metadata_internal_ref__version,
        "metadata_internal_ref_arr_id": facets.metadata_internal_ref_arr_id,
        "metadata_internal_ref_arr_test": facets.metadata_internal_ref_arr_test,
        "metadata_internal_ref_arr__version": facets.metadata_internal_ref_arr__version,
        "metadata_internal_ref_arrobj_id": facets.metadata_internal_ref_arrobj_id,
        "metadata_internal_ref_arrobj_test": facets.metadata_internal_ref_arrobj_test,
        "metadata_internal_ref_arrobj__version": (
            facets.metadata_internal_ref_arrobj__version
        ),
        "metadata_internal_array_ref_array_id": (
            facets.metadata_internal_array_ref_array_id
        ),
        "metadata_internal_array_ref_array_test": (
            facets.metadata_internal_array_ref_array_test
        ),
        "metadata_internal_array_ref_array__version": (
            facets.metadata_internal_array_ref_array__version
        ),
        "metadata_internal_array_object_ref_array_ref_id": (
            facets.metadata_internal_array_object_ref_array_ref_id
        ),
        "metadata_internal_array_object_ref_array_ref_test": (
            facets.metadata_internal_array_object_ref_array_ref_test
        ),
        "metadata_internal_array_object_ref_array_ref__version": (
            facets.metadata_internal_array_object_ref_array_ref__version
        ),
        "metadata_internal_array_nested_ref_arr_id": (
            facets.metadata_internal_array_nested_ref_arr_id
        ),
        "metadata_internal_array_nested_ref_arr_test": (
            facets.metadata_internal_array_nested_ref_arr_test
        ),
        "metadata_internal_array_nested_ref_arr__version": (
            facets.metadata_internal_array_nested_ref_arr__version
        ),
        "metadata_internal_cf_id": facets.metadata_internal_cf_id,
        "metadata_internal_cf_test": facets.metadata_internal_cf_test,
        "metadata_internal_cf__version": facets.metadata_internal_cf__version,
        "metadata_invenio_ref_id": facets.metadata_invenio_ref_id,
        "metadata_invenio_ref__version": facets.metadata_invenio_ref__version,
        "metadata_invenio_array_id": facets.metadata_invenio_array_id,
        "metadata_invenio_array__version": facets.metadata_invenio_array__version,
        "metadata_invenio_nested_ref_id": facets.metadata_invenio_nested_ref_id,
        "metadata_invenio_nested_ref__version": (
            facets.metadata_invenio_nested_ref__version
        ),
        "metadata_invenio_array_nested_ref_arr_id": (
            facets.metadata_invenio_array_nested_ref_arr_id
        ),
        "metadata_invenio_array_nested_ref_arr__version": (
            facets.metadata_invenio_array_nested_ref_arr__version
        ),
        "metadata_ref_id": facets.metadata_ref_id,
        "metadata_ref__version": facets.metadata_ref__version,
        "metadata_array_id": facets.metadata_array_id,
        "metadata_array__version": facets.metadata_array__version,
        "metadata_nested_ref_id": facets.metadata_nested_ref_id,
        "metadata_nested_ref__version": facets.metadata_nested_ref__version,
        "metadata_array_nested_ref_arr_id": facets.metadata_array_nested_ref_arr_id,
        "metadata_array_nested_ref_arr__version": (
            facets.metadata_array_nested_ref_arr__version
        ),
        "metadata_cf_id": facets.metadata_cf_id,
        "metadata_cf_test": facets.metadata_cf_test,
        "metadata_cf__version": facets.metadata_cf__version,
        "_id": facets._id,
        "created": facets.created,
        "updated": facets.updated,
        "_schema": facets._schema,
    }
    sort_options = {
        **InvenioSearchOptions.sort_options,
    }
