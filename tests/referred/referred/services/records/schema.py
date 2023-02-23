import marshmallow as ma
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from marshmallow import fields as ma_fields
from oarepo_runtime.cf import InlinedCustomFieldsSchemaMixin
from oarepo_runtime.validation import validate_date


class ObjarrItemSchema(ma.Schema):
    """ObjarrItemSchema schema."""

    title = ma_fields.String()


class TitleItemSchema(ma.Schema):
    """TitleItemSchema schema."""

    title = ma_fields.String()


class ArrarrItemSchema(ma.Schema):
    """ArrarrItemSchema schema."""

    title = ma_fields.List(ma_fields.Nested(lambda: TitleItemSchema()))


class ReferredMetadataSchema(ma.Schema):
    """ReferredMetadataSchema schema."""

    title = ma_fields.String()
    description = ma_fields.String()
    hint = ma_fields.String()
    price = ma_fields.Float()
    arr = ma_fields.List(ma_fields.String())
    objarr = ma_fields.List(ma_fields.Nested(lambda: ObjarrItemSchema()))
    arrarr = ma_fields.List(ma_fields.Nested(lambda: ArrarrItemSchema()))


class ReferredSchema(InlinedCustomFieldsSchemaMixin, InvenioBaseRecordSchema):
    """ReferredSchema schema."""

    CUSTOM_FIELDS_VAR = "TEST_CF"
    metadata = ma_fields.Nested(lambda: ReferredMetadataSchema())
    created = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
    updated = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
