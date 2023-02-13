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


metadata_ref_id = TermsFacet(field="metadata.ref.id")


metadata_ref__version = TermsFacet(field="metadata.ref.@v")


metadata_array_id = TermsFacet(field="metadata.array.id")


metadata_array__version = TermsFacet(field="metadata.array.@v")


metadata_array = TermsFacet(field="metadata.array")


metadata_nested_ref_id = TermsFacet(field="metadata.nested.ref.id")


metadata_nested_ref__version = TermsFacet(field="metadata.nested.ref.@v")


metadata_nested = TermsFacet(field="metadata.nested")


_id = TermsFacet(field="id")


created = TermsFacet(field="created")


updated = TermsFacet(field="updated")


_schema = TermsFacet(field="$schema")
