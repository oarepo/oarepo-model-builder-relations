"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet

hint = TermsFacet(field="hint")


price = TermsFacet(field="price")


arr = TermsFacet(field="arr")


_id = TermsFacet(field="id")


created = TermsFacet(field="created")


updated = TermsFacet(field="updated")


_schema = TermsFacet(field="$schema")
