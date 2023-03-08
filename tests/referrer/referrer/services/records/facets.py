"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from invenio_search.engine import dsl
from oarepo_runtime.facets.nested_facet import NestedLabeledFacet

metadata_obj_test = TermsFacet(field="metadata.obj.test")


metadata_obj_id = TermsFacet(field="metadata.obj.id")


metadata_arr_test = TermsFacet(field="metadata.arr.test")


metadata_arr_id = TermsFacet(field="metadata.arr.id")


metadata_arrobj_test = TermsFacet(field="metadata.arrobj.test")


metadata_arrobj_id = TermsFacet(field="metadata.arrobj.id")


metadata_internal_ref_id = TermsFacet(field="metadata.internal-ref.id")


metadata_internal_ref_test = TermsFacet(field="metadata.internal-ref.test")


metadata_internal_ref__version = TermsFacet(field="metadata.internal-ref.@v")


metadata_internal_ref_arr_id = TermsFacet(field="metadata.internal-ref-arr.id")


metadata_internal_ref_arr_test = TermsFacet(field="metadata.internal-ref-arr.test")


metadata_internal_ref_arr__version = TermsFacet(field="metadata.internal-ref-arr.@v")


metadata_internal_ref_arrobj_id = TermsFacet(field="metadata.internal-ref-arrobj.id")


metadata_internal_ref_arrobj_test = TermsFacet(
    field="metadata.internal-ref-arrobj.test"
)


metadata_internal_ref_arrobj__version = TermsFacet(
    field="metadata.internal-ref-arrobj.@v"
)


metadata_internal_array_ref_array_id = TermsFacet(
    field="metadata.internal-array-ref-array.id"
)


metadata_internal_array_ref_array_test = TermsFacet(
    field="metadata.internal-array-ref-array.test"
)


metadata_internal_array_ref_array__version = TermsFacet(
    field="metadata.internal-array-ref-array.@v"
)


metadata_internal_array_object_ref_array_ref_id = TermsFacet(
    field="metadata.internal-array-object-ref-array.ref.id"
)


metadata_internal_array_object_ref_array_ref_test = TermsFacet(
    field="metadata.internal-array-object-ref-array.ref.test"
)


metadata_internal_array_object_ref_array_ref__version = TermsFacet(
    field="metadata.internal-array-object-ref-array.ref.@v"
)


metadata_internal_array_nested_ref_arr_id = TermsFacet(
    field="metadata.internal-array-nested.ref-arr.id"
)


metadata_internal_array_nested_ref_arr_test = TermsFacet(
    field="metadata.internal-array-nested.ref-arr.test"
)


metadata_internal_array_nested_ref_arr__version = TermsFacet(
    field="metadata.internal-array-nested.ref-arr.@v"
)


metadata_internal_cf_id = TermsFacet(field="metadata.internal-cf.id")


metadata_internal_cf_test = TermsFacet(field="metadata.internal-cf.test")


metadata_internal_cf__version = TermsFacet(field="metadata.internal-cf.@v")


metadata_invenio_ref_id = TermsFacet(field="metadata.invenio-ref.id")


metadata_invenio_ref__version = TermsFacet(field="metadata.invenio-ref.@v")


metadata_invenio_array_id = TermsFacet(field="metadata.invenio-array.id")


metadata_invenio_array__version = TermsFacet(field="metadata.invenio-array.@v")


metadata_invenio_nested_ref_id = TermsFacet(field="metadata.invenio-nested.ref.id")


metadata_invenio_nested_ref__version = TermsFacet(
    field="metadata.invenio-nested.ref.@v"
)


metadata_invenio_array_nested_ref_arr_id = TermsFacet(
    field="metadata.invenio-array-nested.ref-arr.id"
)


metadata_invenio_array_nested_ref_arr__version = TermsFacet(
    field="metadata.invenio-array-nested.ref-arr.@v"
)


metadata_ref_id = TermsFacet(field="metadata.ref.id")


metadata_ref__version = TermsFacet(field="metadata.ref.@v")


metadata_array_id = TermsFacet(field="metadata.array.id")


metadata_array__version = TermsFacet(field="metadata.array.@v")


metadata_nested_ref_id = TermsFacet(field="metadata.nested.ref.id")


metadata_nested_ref__version = TermsFacet(field="metadata.nested.ref.@v")


metadata_array_nested_ref_arr_id = TermsFacet(field="metadata.array-nested.ref-arr.id")


metadata_array_nested_ref_arr__version = TermsFacet(
    field="metadata.array-nested.ref-arr.@v"
)


metadata_cf_id = TermsFacet(field="metadata.cf.id")


metadata_cf_test = TermsFacet(field="metadata.cf.test")


metadata_cf__version = TermsFacet(field="metadata.cf.@v")


_id = TermsFacet(field="id")


created = TermsFacet(field="created")


updated = TermsFacet(field="updated")


_schema = TermsFacet(field="$schema")
