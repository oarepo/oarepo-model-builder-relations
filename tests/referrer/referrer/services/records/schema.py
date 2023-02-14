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


class ObjSchema(ma.Schema):
    """ObjSchema schema."""

    test = ma_fields.String()
    id = ma_fields.String()


class ArrItemSchema(ma.Schema):
    """ArrItemSchema schema."""

    test = ma_fields.String()
    id = ma_fields.String()


class ArrobjItemSchema(ma.Schema):
    """ArrobjItemSchema schema."""

    test = ma_fields.String()
    id = ma_fields.String()


class InternalRefSchema(ma.Schema):
    """InternalRefSchema schema."""

    id = ma_fields.String()
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalRefArrSchema(ma.Schema):
    """InternalRefArrSchema schema."""

    id = ma_fields.String()
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalRefArrobjSchema(ma.Schema):
    """InternalRefArrobjSchema schema."""

    id = ma_fields.String()
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalArrayRefArrayItemSchema(ma.Schema):
    """InternalArrayRefArrayItemSchema schema."""

    id = ma_fields.String()
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class RefSchema(ma.Schema):
    """RefSchema schema."""

    id = ma_fields.String()
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalArrayNestedItemSchema(ma.Schema):
    """InternalArrayNestedItemSchema schema."""

    ref = ma_fields.Nested(lambda: RefSchema())


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


class InvenioNestedRefSchema(ma.Schema):
    """InvenioNestedRefSchema schema."""

    id = ma_fields.String()
    metadata = ma_fields.Nested(lambda: RefReferredMetadataSchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioNestedItemSchema(ma.Schema):
    """InvenioNestedItemSchema schema."""

    ref = ma_fields.Nested(lambda: InvenioNestedRefSchema())


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

    obj = ma_fields.Nested(lambda: ObjSchema())
    arr = ma_fields.List(ma_fields.Nested(lambda: ArrItemSchema()))
    arrobj = ma_fields.List(ma_fields.Nested(lambda: ArrobjItemSchema()))
    internal_ref = ma_fields.Nested(
        lambda: InternalRefSchema(), data_key="internal-ref", attribute="internal-ref"
    )
    internal_ref_arr = ma_fields.Nested(
        lambda: InternalRefArrSchema(),
        data_key="internal-ref-arr",
        attribute="internal-ref-arr",
    )
    internal_ref_arrobj = ma_fields.Nested(
        lambda: InternalRefArrobjSchema(),
        data_key="internal-ref-arrobj",
        attribute="internal-ref-arrobj",
    )
    internal_array_ref_array = ma_fields.List(
        ma_fields.Nested(lambda: InternalArrayRefArrayItemSchema()),
        data_key="internal-array-ref-array",
        attribute="internal-array-ref-array",
    )
    internal_array_nested = ma_fields.List(
        ma_fields.Nested(lambda: InternalArrayNestedItemSchema()),
        data_key="internal-array-nested",
        attribute="internal-array-nested",
    )
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
