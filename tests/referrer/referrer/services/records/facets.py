"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet

metadata_obj_test = TermsFacet(field="metadata.obj.test")


metadata_obj__id = TermsFacet(field="metadata.obj.id")


metadata_arr_test = TermsFacet(field="metadata.arr.test")


metadata_arr__id = TermsFacet(field="metadata.arr.id")


arrobj_test = TermsFacet(field="arrobj.test")


arrobj__id = TermsFacet(field="arrobj.id")


internal_ref__id = TermsFacet(field="internal-ref.id")


internal_ref_test = TermsFacet(field="internal-ref.test")


internal_ref__version = TermsFacet(field="internal-ref.@v")


internal_ref_arr__id = TermsFacet(field="internal-ref-arr.id")


internal_ref_arr_test = TermsFacet(field="internal-ref-arr.test")


internal_ref_arr__version = TermsFacet(field="internal-ref-arr.@v")


internal_ref_arrobj__id = TermsFacet(field="internal-ref-arrobj.id")


internal_ref_arrobj_test = TermsFacet(field="internal-ref-arrobj.test")


internal_ref_arrobj__version = TermsFacet(field="internal-ref-arrobj.@v")


_id = TermsFacet(field="id")


test = TermsFacet(field="test")


_version = TermsFacet(field="@v")


internal_array_object_ref_array_ref__id = TermsFacet(
    field="internal-array-object-ref-array.ref.id"
)


internal_array_object_ref_array_ref_test = TermsFacet(
    field="internal-array-object-ref-array.ref.test"
)


internal_array_object_ref_array_ref__version = TermsFacet(
    field="internal-array-object-ref-array.ref.@v"
)


internal_array_nested__id = TermsFacet(field="internal-array-nested.id")


test = TermsFacet(field="test")


_version = TermsFacet(field="@v")


internal_cf__id = TermsFacet(field="internal-cf.id")


internal_cf_test = TermsFacet(field="internal-cf.test")


internal_cf__version = TermsFacet(field="internal-cf.@v")


invenio_ref__id = TermsFacet(field="invenio-ref.id")


_version = TermsFacet(field="@v")


_id = TermsFacet(field="id")


_version = TermsFacet(field="@v")


invenio_nested_ref__id = TermsFacet(field="invenio-nested.ref.id")


_version = TermsFacet(field="@v")


invenio_array_nested__id = TermsFacet(field="invenio-array-nested.id")


_version = TermsFacet(field="@v")


ref__id = TermsFacet(field="ref.id")


_version = TermsFacet(field="@v")


_id = TermsFacet(field="id")


_version = TermsFacet(field="@v")


nested_ref__id = TermsFacet(field="nested.ref.id")


_version = TermsFacet(field="@v")


array_nested__id = TermsFacet(field="array-nested.id")


_version = TermsFacet(field="@v")


cf__id = TermsFacet(field="cf.id")


test = TermsFacet(field="test")


_version = TermsFacet(field="@v")


_id = TermsFacet(field="id")


created = TermsFacet(field="created")


updated = TermsFacet(field="updated")


_schema = TermsFacet(field="$schema")
