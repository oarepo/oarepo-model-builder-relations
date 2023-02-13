import marshmallow as ma
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from marshmallow import ValidationError
from marshmallow import fields as ma_fields
from marshmallow import validates as ma_validates
from marshmallow_utils import fields as mu_fields
from marshmallow_utils import schemas as mu_schemas
from oarepo_runtime.validation import validate_date


class InvenioRefReferredMetadataSchema(ma.Schema):
    """InvenioRefReferredMetadataSchema schema."""

    title = ma_fields.String()


class InvenioRefSchema(ma.Schema):
    """InvenioRefSchema schema."""

    id = ma_fields.String()
    metadata = ma_fields.Nested(lambda: InvenioRefReferredMetadataSchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioArrayItemReferredMetadataSchema(ma.Schema):
    """InvenioArrayItemReferredMetadataSchema schema."""

    title = ma_fields.String()


class InvenioArrayItemSchema(ma.Schema):
    """InvenioArrayItemSchema schema."""

    id = ma_fields.String()
    metadata = ma_fields.Nested(lambda: InvenioArrayItemReferredMetadataSchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class RefReferredMetadataSchema(ma.Schema):
    """RefReferredMetadataSchema schema."""

    title = ma_fields.String()


class RefSchema(ma.Schema):
    """RefSchema schema."""

    id = ma_fields.String()
    metadata = ma_fields.Nested(lambda: RefReferredMetadataSchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioNestedItemSchema(ma.Schema):
    """InvenioNestedItemSchema schema."""

    ref = ma_fields.Nested(lambda: RefSchema())


class RefArrItemReferredMetadataSchema(ma.Schema):
    """RefArrItemReferredMetadataSchema schema."""

    title = ma_fields.String()


class RefArrItemSchema(ma.Schema):
    """RefArrItemSchema schema."""

    id = ma_fields.String()
    metadata = ma_fields.Nested(lambda: RefArrItemReferredMetadataSchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioArrayNestedItemSchema(ma.Schema):
    """InvenioArrayNestedItemSchema schema."""

    ref_arr = ma_fields.List(
        ma_fields.Nested(lambda: RefArrItemSchema()),
        data_key="ref-arr",
        attribute="ref-arr",
    )


class MetadataRefSchema(ma.Schema):
    """MetadataRefSchema schema."""

    id = ma_fields.String()
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class ArrayItemSchema(ma.Schema):
    """ArrayItemSchema schema."""

    id = ma_fields.String()
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NestedRefSchema(ma.Schema):
    """NestedRefSchema schema."""

    id = ma_fields.String()
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NestedItemSchema(ma.Schema):
    """NestedItemSchema schema."""

    ref = ma_fields.Nested(lambda: NestedRefSchema())


class RefArrRefArrItemSchema(ma.Schema):
    """RefArrRefArrItemSchema schema."""

    id = ma_fields.String()
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class ArrayNestedItemSchema(ma.Schema):
    """ArrayNestedItemSchema schema."""

    ref_arr = ma_fields.List(
        ma_fields.Nested(lambda: RefArrRefArrItemSchema()),
        data_key="ref-arr",
        attribute="ref-arr",
    )


class CfSchema(ma.Schema):
    """CfSchema schema."""

    id = ma_fields.String()
    title = ma_fields.String()
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class ReferrerMetadataSchema(ma.Schema):
    """ReferrerMetadataSchema schema."""

    invenio_ref = ma_fields.Nested(
        lambda: InvenioRefSchema(), data_key="invenio-ref", attribute="invenio-ref"
    )
    invenio_array = ma_fields.List(
        ma_fields.Nested(lambda: InvenioArrayItemSchema()),
        data_key="invenio-array",
        attribute="invenio-array",
    )
    invenio_nested = ma_fields.List(
        ma_fields.Nested(lambda: InvenioNestedItemSchema()),
        data_key="invenio-nested",
        attribute="invenio-nested",
    )
    invenio_array_nested = ma_fields.List(
        ma_fields.Nested(lambda: InvenioArrayNestedItemSchema()),
        data_key="invenio-array-nested",
        attribute="invenio-array-nested",
    )
    ref = ma_fields.Nested(lambda: MetadataRefSchema())
    array = ma_fields.List(ma_fields.Nested(lambda: ArrayItemSchema()))
    nested = ma_fields.List(ma_fields.Nested(lambda: NestedItemSchema()))
    array_nested = ma_fields.List(
        ma_fields.Nested(lambda: ArrayNestedItemSchema()),
        data_key="array-nested",
        attribute="array-nested",
    )
    cf = ma_fields.Nested(lambda: CfSchema())


class ReferrerSchema(InvenioBaseRecordSchema):
    """ReferrerSchema schema."""

    metadata = ma_fields.Nested(lambda: ReferrerMetadataSchema())
    created = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
    updated = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
