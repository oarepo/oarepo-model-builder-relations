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


class ReferredMetadataSchema(ma.Schema):
    """ReferredMetadataSchema schema."""

    title = ma_fields.String()
    description = ma_fields.String()
    hint = ma_fields.String()
    price = ma_fields.Float()


class ReferredSchema(InvenioBaseRecordSchema):
    """ReferredSchema schema."""

    metadata = ma_fields.Nested(lambda: ReferredMetadataSchema())
    created = ma_fields.String(validate=[validate_date("%Y:%m:%d")], dump_only=True)
    updated = ma_fields.String(validate=[validate_date("%Y:%m:%d")], dump_only=True)
