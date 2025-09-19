from .database import db
from geoalchemy2 import Geometry
from sqlalchemy.dialects.postgresql import JSONB

# -------------------
# 1. Holders Table
# -------------------
class Holder(db.Model):
    __tablename__ = "holders"

    holder_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    tribe_name = db.Column(db.String(100))
    village_name = db.Column(db.String(150))
    district_name = db.Column(db.String(150))
    state_name = db.Column(db.String(100))
    contact_info = db.Column(JSONB)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    # Relationships
    claims = db.relationship("Claim", backref="holder", cascade="all, delete-orphan")
    schemes = db.relationship("HolderScheme", backref="holder", cascade="all, delete-orphan")


# -------------------
# 2. Claims Table
# -------------------
class Claim(db.Model):
    __tablename__ = "claims"

    claim_id = db.Column(db.Integer, primary_key=True)
    holder_id = db.Column(db.Integer, db.ForeignKey("holders.holder_id"), nullable=False)
    claim_type = db.Column(db.String(10))  # IFR, CR, CFR
    claim_status = db.Column(db.String(50))  # Pending, Verified, Approved, Rejected
    claim_date = db.Column(db.Date)
    granted_area = db.Column(db.Float)  # hectares
    claim_geometry = db.Column(Geometry("POLYGON", 4326))
    supporting_docs = db.Column(JSONB)

    # Relationships
    assets = db.relationship("Asset", backref="claim", cascade="all, delete-orphan")
    documents = db.relationship("Document", backref="claim", cascade="all, delete-orphan")


# -------------------
# 3. Assets Table
# -------------------
class Asset(db.Model):
    __tablename__ = "assets"

    asset_id = db.Column(db.Integer, primary_key=True)
    claim_id = db.Column(db.Integer, db.ForeignKey("claims.claim_id"), nullable=False)
    asset_type = db.Column(db.String(50))  # Pond, Farm, Forest, etc.
    description = db.Column(db.Text)
    asset_geometry = db.Column(Geometry("GEOMETRY", 4326))
    area = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


# -------------------
# 4. Documents Table
# -------------------
class Document(db.Model):
    __tablename__ = "documents"

    doc_id = db.Column(db.Integer, primary_key=True)
    claim_id = db.Column(db.Integer, db.ForeignKey("claims.claim_id"), nullable=False)
    file_path = db.Column(db.Text)
    ocr_text = db.Column(db.Text)
    processed = db.Column(db.Boolean, default=False)
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())


# -------------------
# 5. Schemes + HolderSchemes
# -------------------
class Scheme(db.Model):
    __tablename__ = "schemes"

    scheme_id = db.Column(db.Integer, primary_key=True)
    scheme_name = db.Column(db.String(150))
    ministry = db.Column(db.String(150))
    eligibility_criteria = db.Column(JSONB)
    description = db.Column(db.Text)

    # Relationships
    holders = db.relationship("HolderScheme", backref="scheme", cascade="all, delete-orphan")


class HolderScheme(db.Model):
    __tablename__ = "holder_schemes"

    id = db.Column(db.Integer, primary_key=True)
    holder_id = db.Column(db.Integer, db.ForeignKey("holders.holder_id"), nullable=False)
    scheme_id = db.Column(db.Integer, db.ForeignKey("schemes.scheme_id"), nullable=False)
    status = db.Column(db.String(50))  # Eligible, Not Eligible, Granted
    assigned_at = db.Column(db.DateTime, server_default=db.func.now())
