from invenio_db import db
from invenio_records.models import RecordMetadataBase


class ReferredMetadata(db.Model, RecordMetadataBase):
    """Model for ReferredRecord metadata."""

    __tablename__ = "referred_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
