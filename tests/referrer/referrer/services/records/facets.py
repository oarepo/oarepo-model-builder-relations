"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from invenio_search.engine import dsl


class NestedLabeledFacet(dsl.Facet):
    agg_type = "nested"

    def __init__(self, path, nested_facet, label=""):
        self._path = path
        self._inner = nested_facet
        self._label = label
        super(NestedLabeledFacet, self).__init__(
            path=path,
            aggs={
                "inner": nested_facet.get_aggregation(),
            },
        )

    def get_values(self, data, filter_values):
        return self._inner.get_values(data.inner, filter_values)

    def add_filter(self, filter_values):
        inner_q = self._inner.add_filter(filter_values)
        if inner_q:
            return dsl.Nested(path=self._path, query=inner_q)

    def get_labelled_values(self, data, filter_values):
        """Get a labelled version of a bucket."""
        try:
            out = data["buckets"]
        except:
            out = []
        return {"buckets": out, "label": str(self._label)}


metadata_obj_test = TermsFacet(field="metadata.obj.test")


metadata_obj_id = TermsFacet(field="metadata.obj.id")


metadata_arr_test = TermsFacet(field="metadata.arr.test")


metadata_arr_id = TermsFacet(field="metadata.arr.id")


metadata_arr = TermsFacet(field="metadata.arr")


metadata_arrobj_test = TermsFacet(field="metadata.arrobj.test")


metadata_arrobj_id = TermsFacet(field="metadata.arrobj.id")


metadata_arrobj = TermsFacet(field="metadata.arrobj")


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


metadata_internal_array_ref_array = TermsFacet(
    field="metadata.internal-array-ref-array"
)


metadata_internal_array_nested_ref_id = TermsFacet(
    field="metadata.internal-array-nested.ref.id"
)


metadata_internal_array_nested_ref_test = TermsFacet(
    field="metadata.internal-array-nested.ref.test"
)


metadata_internal_array_nested_ref__version = TermsFacet(
    field="metadata.internal-array-nested.ref.@v"
)


metadata_internal_array_nested = TermsFacet(field="metadata.internal-array-nested")


metadata_invenio_ref_id = TermsFacet(field="metadata.invenio-ref.id")


metadata_invenio_ref__version = TermsFacet(field="metadata.invenio-ref.@v")


metadata_invenio_array_id = TermsFacet(field="metadata.invenio-array.id")


metadata_invenio_array__version = TermsFacet(field="metadata.invenio-array.@v")


metadata_invenio_array = TermsFacet(field="metadata.invenio-array")


metadata_invenio_nested_ref_id = TermsFacet(field="metadata.invenio-nested.ref.id")


metadata_invenio_nested_ref__version = TermsFacet(
    field="metadata.invenio-nested.ref.@v"
)


metadata_invenio_nested = TermsFacet(field="metadata.invenio-nested")


metadata_invenio_array_nested_ref_arr_id = TermsFacet(
    field="metadata.invenio-array-nested.ref-arr.id"
)


metadata_invenio_array_nested_ref_arr__version = TermsFacet(
    field="metadata.invenio-array-nested.ref-arr.@v"
)


metadata_invenio_array_nested_ref_arr = TermsFacet(
    field="metadata.invenio-array-nested.ref-arr"
)


metadata_invenio_array_nested = TermsFacet(field="metadata.invenio-array-nested")


metadata_ref_id = TermsFacet(field="metadata.ref.id")


metadata_ref__version = TermsFacet(field="metadata.ref.@v")


metadata_array_id = TermsFacet(field="metadata.array.id")


metadata_array__version = TermsFacet(field="metadata.array.@v")


metadata_array = TermsFacet(field="metadata.array")


metadata_nested_ref_id = TermsFacet(field="metadata.nested.ref.id")


metadata_nested_ref__version = TermsFacet(field="metadata.nested.ref.@v")


metadata_nested = TermsFacet(field="metadata.nested")


metadata_array_nested_ref_arr_id = TermsFacet(field="metadata.array-nested.ref-arr.id")


metadata_array_nested_ref_arr__version = TermsFacet(
    field="metadata.array-nested.ref-arr.@v"
)


metadata_array_nested_ref_arr = TermsFacet(field="metadata.array-nested.ref-arr")


metadata_array_nested = TermsFacet(field="metadata.array-nested")


metadata_cf_id = TermsFacet(field="metadata.cf.id")


metadata_cf_test = TermsFacet(field="metadata.cf.test")


metadata_cf__version = TermsFacet(field="metadata.cf.@v")


_id = TermsFacet(field="id")


created = TermsFacet(field="created")


updated = TermsFacet(field="updated")


_schema = TermsFacet(field="$schema")
