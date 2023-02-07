from invenio_db import db
from invenio_records.models import RecordMetadataBase


class ReferrerMetadata(db.Model, RecordMetadataBase):
    """Model for ReferrerRecord metadata."""

    __tablename__ = "referrer_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
