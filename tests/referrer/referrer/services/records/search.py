from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


def _(x):
    """Identity function for string extraction."""
    return x


class ReferrerSearchOptions(InvenioSearchOptions):
    """ReferrerRecord search options."""

    facets = {
        "metadata_obj_test": facets.metadata_obj_test,
        "metadata_obj__id": facets.metadata_obj__id,
        "metadata_arr_test": facets.metadata_arr_test,
        "metadata_arr__id": facets.metadata_arr__id,
        "arrobj_test": facets.arrobj_test,
        "arrobj__id": facets.arrobj__id,
        "internal_ref__id": facets.internal_ref__id,
        "internal_ref_test": facets.internal_ref_test,
        "internal_ref__version": facets.internal_ref__version,
        "internal_ref_arr__id": facets.internal_ref_arr__id,
        "internal_ref_arr_test": facets.internal_ref_arr_test,
        "internal_ref_arr__version": facets.internal_ref_arr__version,
        "internal_ref_arrobj__id": facets.internal_ref_arrobj__id,
        "internal_ref_arrobj_test": facets.internal_ref_arrobj_test,
        "internal_ref_arrobj__version": facets.internal_ref_arrobj__version,
        "_id": facets._id,
        "test": facets.test,
        "_version": facets._version,
        "internal_array_object_ref_array_ref__id": (
            facets.internal_array_object_ref_array_ref__id
        ),
        "internal_array_object_ref_array_ref_test": (
            facets.internal_array_object_ref_array_ref_test
        ),
        "internal_array_object_ref_array_ref__version": (
            facets.internal_array_object_ref_array_ref__version
        ),
        "internal_array_nested__id": facets.internal_array_nested__id,
        "test": facets.test,
        "_version": facets._version,
        "internal_cf__id": facets.internal_cf__id,
        "internal_cf_test": facets.internal_cf_test,
        "internal_cf__version": facets.internal_cf__version,
        "invenio_ref__id": facets.invenio_ref__id,
        "_version": facets._version,
        "_id": facets._id,
        "_version": facets._version,
        "invenio_nested_ref__id": facets.invenio_nested_ref__id,
        "_version": facets._version,
        "invenio_array_nested__id": facets.invenio_array_nested__id,
        "_version": facets._version,
        "ref__id": facets.ref__id,
        "_version": facets._version,
        "_id": facets._id,
        "_version": facets._version,
        "nested_ref__id": facets.nested_ref__id,
        "_version": facets._version,
        "array_nested__id": facets.array_nested__id,
        "_version": facets._version,
        "cf__id": facets.cf__id,
        "test": facets.test,
        "_version": facets._version,
        "_id": facets._id,
        "created": facets.created,
        "updated": facets.updated,
        "_schema": facets._schema,
    }
    sort_options = {
        **InvenioSearchOptions.sort_options,
    }
