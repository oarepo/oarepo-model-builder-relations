import marshmallow as ma
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from marshmallow import ValidationError
from marshmallow import fields as ma_fields
from marshmallow import validate as ma_validate
from marshmallow_utils import fields as mu_fields
from marshmallow_utils import schemas as mu_schemas
from oarepo_runtime.ui import marshmallow as l10n
from oarepo_runtime.validation import validate_date


class ObjUISchema(ma.Schema):
    """ObjUISchema schema."""

    test = ma_fields.String()
    _id = ma_fields.String(data_key="id", attribute="id")


class ArrItemUISchema(ma.Schema):
    """ArrItemUISchema schema."""

    test = ma_fields.String()
    _id = ma_fields.String(data_key="id", attribute="id")


class ArrobjItemUISchema(ma.Schema):
    """ArrobjItemUISchema schema."""

    test = ma_fields.String()
    _id = ma_fields.String(data_key="id", attribute="id")


class InternalRefUISchema(ma.Schema):
    """InternalRefUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalRefArrUISchema(ma.Schema):
    """InternalRefArrUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalRefArrobjUISchema(ma.Schema):
    """InternalRefArrobjUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalArrayRefArrayItemUISchema(ma.Schema):
    """InternalArrayRefArrayItemUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class RefUISchema(ma.Schema):
    """RefUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalArrayObjectRefArrayItemUISchema(ma.Schema):
    """InternalArrayObjectRefArrayItemUISchema schema."""

    ref = ma_fields.Nested(lambda: RefUISchema())


class RefArrRefArrItemUISchema(ma.Schema):
    """RefArrRefArrItemUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InternalArrayNestedItemUISchema(ma.Schema):
    """InternalArrayNestedItemUISchema schema."""

    ref_arr = ma_fields.List(
        ma_fields.Nested(lambda: RefArrRefArrItemUISchema()),
        data_key="ref-arr",
        attribute="ref-arr",
    )


class InternalCfUISchema(ma.Schema):
    """InternalCfUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class MetadataUISchema(ma.Schema):
    """MetadataUISchema schema."""

    title = ma_fields.String()


class InvenioRefUISchema(ma.Schema):
    """InvenioRefUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    metadata = ma_fields.Nested(lambda: MetadataUISchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioArrayItemUISchema(ma.Schema):
    """InvenioArrayItemUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    metadata = ma_fields.Nested(lambda: MetadataUISchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioNestedRefUISchema(ma.Schema):
    """InvenioNestedRefUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    metadata = ma_fields.Nested(lambda: MetadataUISchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioNestedItemUISchema(ma.Schema):
    """InvenioNestedItemUISchema schema."""

    ref = ma_fields.Nested(lambda: InvenioNestedRefUISchema())


class InvenioArrayNestedRefArrRefArrItemUISchema(ma.Schema):
    """InvenioArrayNestedRefArrRefArrItemUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    metadata = ma_fields.Nested(lambda: MetadataUISchema())
    _version = ma_fields.String(data_key="@v", attribute="@v")


class InvenioArrayNestedItemUISchema(ma.Schema):
    """InvenioArrayNestedItemUISchema schema."""

    ref_arr = ma_fields.List(
        ma_fields.Nested(lambda: InvenioArrayNestedRefArrRefArrItemUISchema()),
        data_key="ref-arr",
        attribute="ref-arr",
    )


class MetadataRefUISchema(ma.Schema):
    """MetadataRefUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class ArrayItemUISchema(ma.Schema):
    """ArrayItemUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NestedRefUISchema(ma.Schema):
    """NestedRefUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class NestedItemUISchema(ma.Schema):
    """NestedItemUISchema schema."""

    ref = ma_fields.Nested(lambda: NestedRefUISchema())


class RefArrItemUISchema(ma.Schema):
    """RefArrItemUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class ArrayNestedItemUISchema(ma.Schema):
    """ArrayNestedItemUISchema schema."""

    ref_arr = ma_fields.List(
        ma_fields.Nested(lambda: RefArrItemUISchema()),
        data_key="ref-arr",
        attribute="ref-arr",
    )


class CfUISchema(ma.Schema):
    """CfUISchema schema."""

    _id = ma_fields.String(data_key="id", attribute="id")
    title = ma_fields.String()
    test = ma_fields.String()
    _version = ma_fields.String(data_key="@v", attribute="@v")


class ReferrerMetadataUISchema(ma.Schema):
    """ReferrerMetadataUISchema schema."""

    obj = ma_fields.Nested(lambda: ObjUISchema())
    arr = ma_fields.List(ma_fields.Nested(lambda: ArrItemUISchema()))
    arrobj = ma_fields.List(ma_fields.Nested(lambda: ArrobjItemUISchema()))
    internal_ref = ma_fields.Nested(
        lambda: InternalRefUISchema(), data_key="internal-ref", attribute="internal-ref"
    )
    internal_ref_arr = ma_fields.Nested(
        lambda: InternalRefArrUISchema(),
        data_key="internal-ref-arr",
        attribute="internal-ref-arr",
    )
    internal_ref_arrobj = ma_fields.Nested(
        lambda: InternalRefArrobjUISchema(),
        data_key="internal-ref-arrobj",
        attribute="internal-ref-arrobj",
    )
    internal_array_ref_array = ma_fields.List(
        ma_fields.Nested(lambda: InternalArrayRefArrayItemUISchema()),
        data_key="internal-array-ref-array",
        attribute="internal-array-ref-array",
    )
    internal_array_object_ref_array = ma_fields.List(
        ma_fields.Nested(lambda: InternalArrayObjectRefArrayItemUISchema()),
        data_key="internal-array-object-ref-array",
        attribute="internal-array-object-ref-array",
    )
    internal_array_nested = ma_fields.List(
        ma_fields.Nested(lambda: InternalArrayNestedItemUISchema()),
        data_key="internal-array-nested",
        attribute="internal-array-nested",
    )
    internal_cf = ma_fields.Nested(
        lambda: InternalCfUISchema(), data_key="internal-cf", attribute="internal-cf"
    )
    invenio_ref = ma_fields.Nested(
        lambda: InvenioRefUISchema(), data_key="invenio-ref", attribute="invenio-ref"
    )
    invenio_array = ma_fields.List(
        ma_fields.Nested(lambda: InvenioArrayItemUISchema()),
        data_key="invenio-array",
        attribute="invenio-array",
    )
    invenio_nested = ma_fields.List(
        ma_fields.Nested(lambda: InvenioNestedItemUISchema()),
        data_key="invenio-nested",
        attribute="invenio-nested",
    )
    invenio_array_nested = ma_fields.List(
        ma_fields.Nested(lambda: InvenioArrayNestedItemUISchema()),
        data_key="invenio-array-nested",
        attribute="invenio-array-nested",
    )
    ref = ma_fields.Nested(lambda: MetadataRefUISchema())
    array = ma_fields.List(ma_fields.Nested(lambda: ArrayItemUISchema()))
    nested = ma_fields.List(ma_fields.Nested(lambda: NestedItemUISchema()))
    array_nested = ma_fields.List(
        ma_fields.Nested(lambda: ArrayNestedItemUISchema()),
        data_key="array-nested",
        attribute="array-nested",
    )
    cf = ma_fields.Nested(lambda: CfUISchema())


class ReferrerUISchema(ma.Schema):
    """ReferrerUISchema schema."""

    metadata = ma_fields.Nested(lambda: ReferrerMetadataUISchema())
    _id = ma_fields.String(data_key="id", attribute="id")
    created = l10n.LocalizedDate()
    updated = l10n.LocalizedDate()
    _schema = ma_fields.String(data_key="$schema", attribute="$schema")
