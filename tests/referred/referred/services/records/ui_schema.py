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


class ObjarrItemUISchema(ma.Schema):
    """ObjarrItemUISchema schema."""

    title = ma_fields.String()


class TitleItemUISchema(ma.Schema):
    """TitleItemUISchema schema."""

    title = ma_fields.String()


class ArrarrItemUISchema(ma.Schema):
    """ArrarrItemUISchema schema."""

    title = ma_fields.List(ma_fields.Nested(lambda: TitleItemUISchema()))


class ReferredMetadataUISchema(ma.Schema):
    """ReferredMetadataUISchema schema."""

    title = ma_fields.String()
    description = ma_fields.String()
    hint = ma_fields.String()
    price = ma_fields.Float()
    arr = ma_fields.List(ma_fields.String())
    objarr = ma_fields.List(ma_fields.Nested(lambda: ObjarrItemUISchema()))
    arrarr = ma_fields.List(ma_fields.Nested(lambda: ArrarrItemUISchema()))


class ReferredUISchema(ma.Schema):
    """ReferredUISchema schema."""

    metadata = ma_fields.Nested(lambda: ReferredMetadataUISchema())
    _id = ma_fields.String(data_key="id", attribute="id")
    created = l10n.LocalizedDate()
    updated = l10n.LocalizedDate()
    _schema = ma_fields.String(data_key="$schema", attribute="$schema")
