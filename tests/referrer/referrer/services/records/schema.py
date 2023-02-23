import marshmallow as ma
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from marshmallow import fields as ma_fields
from oarepo_runtime.cf import InlinedCustomFieldsSchemaMixin
from oarepo_runtime.validation import validate_date


class ObjSchema(ma.Schema):
    """ObjSchema schema."""

    test = ma_fields.String()
    _id = ma_fields.String(data_key="id", attribute="id")


class ArrItemSchema(ma.Schema):
    """ArrItemSchema schema."""

    test = ma_fields.String()
    _id = ma_fields.String(data_key="id", attribute="id")


class ArrobjItemSchema(ma.Schema):
    """ArrobjItemSchema schema."""

    test = ma_fields.String()
    _id = ma_fields.String(data_key="id", attribute="id")


class InternalRefSchema(ma.Schema):
    """InternalRefSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalRefArrSchema(ma.Schema):
    """InternalRefArrSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalRefArrobjSchema(ma.Schema):
    """InternalRefArrobjSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalArrayRefArrayItemSchema(ma.Schema):
    """InternalArrayRefArrayItemSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class RefSchema(ma.Schema):
    """RefSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalArrayObjectRefArrayItemSchema(ma.Schema):
    """InternalArrayObjectRefArrayItemSchema schema."""

    ref = ma_fields.Nested(lambda: RefSchema())


class RefArrItemSchema(ma.Schema):
    """RefArrItemSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalArrayNestedItemSchema(ma.Schema):
    """InternalArrayNestedItemSchema schema."""

    ref_arr = ma_fields.List(
        ma_fields.Nested(lambda: RefArrItemSchema()),
        data_key="ref-arr",
        attribute="ref-arr",
    )


class InternalCfSchema(ma.Schema):
    """InternalCfSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class MetadataSchema(ma.Schema):
    """MetadataSchema schema."""

    title = ma_fields.String()


class InvenioRefSchema(ma.Schema):
    """InvenioRefSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    metadata = ma_fields.Nested(lambda: MetadataSchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioArrayItemSchema(ma.Schema):
    """InvenioArrayItemSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    metadata = ma_fields.Nested(lambda: MetadataSchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioNestedRefSchema(ma.Schema):
    """InvenioNestedRefSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    metadata = ma_fields.Nested(lambda: MetadataSchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioNestedItemSchema(ma.Schema):
    """InvenioNestedItemSchema schema."""

    ref = ma_fields.Nested(lambda: InvenioNestedRefSchema())


class RefArrRefArrItemSchema(ma.Schema):
    """RefArrRefArrItemSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    metadata = ma_fields.Nested(lambda: MetadataSchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioArrayNestedItemSchema(ma.Schema):
    """InvenioArrayNestedItemSchema schema."""

    ref_arr = ma_fields.List(
        ma_fields.Nested(lambda: RefArrRefArrItemSchema()),
        data_key="ref-arr",
        attribute="ref-arr",
    )


class MetadataRefSchema(ma.Schema):
    """MetadataRefSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class ArrayItemSchema(ma.Schema):
    """ArrayItemSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NestedRefSchema(ma.Schema):
    """NestedRefSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NestedItemSchema(ma.Schema):
    """NestedItemSchema schema."""

    ref = ma_fields.Nested(lambda: NestedRefSchema())


class ArrayNestedRefArrRefArrItemSchema(ma.Schema):
    """ArrayNestedRefArrRefArrItemSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class ArrayNestedItemSchema(ma.Schema):
    """ArrayNestedItemSchema schema."""

    ref_arr = ma_fields.List(
        ma_fields.Nested(lambda: ArrayNestedRefArrRefArrItemSchema()),
        data_key="ref-arr",
        attribute="ref-arr",
    )


class CfSchema(ma.Schema):
    """CfSchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
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
    internal_array_object_ref_array = ma_fields.List(
        ma_fields.Nested(lambda: InternalArrayObjectRefArrayItemSchema()),
        data_key="internal-array-object-ref-array",
        attribute="internal-array-object-ref-array",
    )
    internal_array_nested = ma_fields.List(
        ma_fields.Nested(lambda: InternalArrayNestedItemSchema()),
        data_key="internal-array-nested",
        attribute="internal-array-nested",
    )
    internal_cf = ma_fields.Nested(
        lambda: InternalCfSchema(), data_key="internal-cf", attribute="internal-cf"
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


class ReferrerSchema(InlinedCustomFieldsSchemaMixin, InvenioBaseRecordSchema):
    """ReferrerSchema schema."""

    CUSTOM_FIELDS_VAR = "TEST_CF"
    metadata = ma_fields.Nested(lambda: ReferrerMetadataSchema())
    created = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
    updated = ma_fields.String(validate=[validate_date("%Y-%m-%d")], dump_only=True)
