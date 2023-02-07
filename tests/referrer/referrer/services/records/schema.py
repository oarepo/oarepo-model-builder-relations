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


class RefReferredMetadataSchema(ma.Schema):
    """RefReferredMetadataSchema schema."""

    title = ma_fields.String()


class RefSchema(ma.Schema):
    """RefSchema schema."""

    id = ma_fields.String()
    metadata = ma_fields.Nested(lambda: RefReferredMetadataSchema())
    _version = ma_fields.String()


class ReferrerMetadataSchema(ma.Schema):
    """ReferrerMetadataSchema schema."""

    ref = ma_fields.Nested(lambda: RefSchema())


class ReferrerSchema(InvenioBaseRecordSchema):
    """ReferrerSchema schema."""

    metadata = ma_fields.Nested(lambda: ReferrerMetadataSchema())
    created = ma_fields.String(validate=[validate_date("%Y:%m:%d")], dump_only=True)
    updated = ma_fields.String(validate=[validate_date("%Y:%m:%d")], dump_only=True)
