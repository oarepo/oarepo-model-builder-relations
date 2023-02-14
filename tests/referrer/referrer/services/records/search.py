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
        "metadata_arr": facets.metadata_arr,
        "metadata_arrobj_test": facets.metadata_arrobj_test,
        "metadata_arrobj_id": facets.metadata_arrobj_id,
        "metadata_arrobj": facets.metadata_arrobj,
        "metadata_internal-ref_id": facets.metadata_internal_ref_id,
        "metadata_internal-ref_test": facets.metadata_internal_ref_test,
        "metadata_internal-ref_@v": facets.metadata_internal_ref__version,
        "metadata_internal-ref-arr_id": facets.metadata_internal_ref_arr_id,
        "metadata_internal-ref-arr_test": facets.metadata_internal_ref_arr_test,
        "metadata_internal-ref-arr_@v": facets.metadata_internal_ref_arr__version,
        "metadata_internal-ref-arrobj_id": facets.metadata_internal_ref_arrobj_id,
        "metadata_internal-ref-arrobj_test": facets.metadata_internal_ref_arrobj_test,
        "metadata_internal-ref-arrobj_@v": facets.metadata_internal_ref_arrobj__version,
        "metadata_internal-array-ref-array_id": (
            facets.metadata_internal_array_ref_array_id
        ),
        "metadata_internal-array-ref-array_test": (
            facets.metadata_internal_array_ref_array_test
        ),
        "metadata_internal-array-ref-array_@v": (
            facets.metadata_internal_array_ref_array__version
        ),
        "metadata_internal-array-ref-array": facets.metadata_internal_array_ref_array,
        "metadata_internal-array-object-ref-array_ref_id": (
            facets.metadata_internal_array_object_ref_array_ref_id
        ),
        "metadata_internal-array-object-ref-array_ref_test": (
            facets.metadata_internal_array_object_ref_array_ref_test
        ),
        "metadata_internal-array-object-ref-array_ref_@v": (
            facets.metadata_internal_array_object_ref_array_ref__version
        ),
        "metadata_internal-array-object-ref-array": (
            facets.metadata_internal_array_object_ref_array
        ),
        "metadata_internal-array-nested_ref-arr_id": (
            facets.metadata_internal_array_nested_ref_arr_id
        ),
        "metadata_internal-array-nested_ref-arr_test": (
            facets.metadata_internal_array_nested_ref_arr_test
        ),
        "metadata_internal-array-nested_ref-arr_@v": (
            facets.metadata_internal_array_nested_ref_arr__version
        ),
        "metadata_internal-array-nested_ref-arr": (
            facets.metadata_internal_array_nested_ref_arr
        ),
        "metadata_internal-array-nested": facets.metadata_internal_array_nested,
        "metadata_internal-cf_id": facets.metadata_internal_cf_id,
        "metadata_internal-cf_test": facets.metadata_internal_cf_test,
        "metadata_internal-cf_@v": facets.metadata_internal_cf__version,
        "metadata_invenio-ref_id": facets.metadata_invenio_ref_id,
        "metadata_invenio-ref_@v": facets.metadata_invenio_ref__version,
        "metadata_invenio-array_id": facets.metadata_invenio_array_id,
        "metadata_invenio-array_@v": facets.metadata_invenio_array__version,
        "metadata_invenio-array": facets.metadata_invenio_array,
        "metadata_invenio-nested_ref_id": facets.metadata_invenio_nested_ref_id,
        "metadata_invenio-nested_ref_@v": facets.metadata_invenio_nested_ref__version,
        "metadata_invenio-nested": facets.metadata_invenio_nested,
        "metadata_invenio-array-nested_ref-arr_id": (
            facets.metadata_invenio_array_nested_ref_arr_id
        ),
        "metadata_invenio-array-nested_ref-arr_@v": (
            facets.metadata_invenio_array_nested_ref_arr__version
        ),
        "metadata_invenio-array-nested_ref-arr": (
            facets.metadata_invenio_array_nested_ref_arr
        ),
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
        "metadata_array-nested_ref-arr_@v": (
            facets.metadata_array_nested_ref_arr__version
        ),
        "metadata_array-nested_ref-arr": facets.metadata_array_nested_ref_arr,
        "metadata_array-nested": facets.metadata_array_nested,
        "metadata_cf_id": facets.metadata_cf_id,
        "metadata_cf_test": facets.metadata_cf_test,
        "metadata_cf_@v": facets.metadata_cf__version,
        "_id": facets._id,
        "created": facets.created,
        "updated": facets.updated,
        "_schema": facets._schema,
    }
    sort_options = {
        **InvenioSearchOptions.sort_options,
    }
