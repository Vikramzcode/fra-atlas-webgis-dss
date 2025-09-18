from flask import Blueprint, jsonify, request
from sqlalchemy import func
from sqlalchemy import text
from geoalchemy2.functions import ST_AsGeoJSON
from .models import Holder, Claim
from .database import db
import json

bp = Blueprint("api", __name__, url_prefix="/api")

# --- Health Check ---
@bp.route("/health", methods=["GET"])
def health_check():
    """Checks if the backend is running."""
    return jsonify({"status": "ok", "message": "Backend running"}), 200

# --- Holder CRUD Endpoints ---
@bp.route("/holders", methods=["POST"])
def create_holder():
    """Creates a new holder."""
    data = request.json
    if not data or 'first_name' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_holder = Holder(**data)
    db.session.add(new_holder)
    db.session.commit()
    return jsonify({"message": "Holder created", "holder_id": new_holder.holder_id}), 201

@bp.route("/holders", methods=["GET"])
def get_all_holders():
    """Gets all holders."""
    holders = Holder.query.all()
    return jsonify([{"holder_id": h.holder_id, "name": f"{h.first_name} {h.last_name}", "village": h.village_name} for h in holders])

@bp.route("/holders/<int:holder_id>", methods=["GET"])
def get_holder(holder_id):
    """Gets a single holder by ID."""
    holder = Holder.query.get_or_404(holder_id)
    return jsonify({
        "holder_id": holder.holder_id,
        "first_name": holder.first_name,
        "last_name": holder.last_name,
        "village_name": holder.village_name
    })

# --- Claim Endpoints ---
@bp.route("/holders/<int:holder_id>/claims", methods=["POST"])
def create_claim_for_holder(holder_id):
    """Creates a new claim for a specific holder."""
    Holder.query.get_or_404(holder_id) # Ensure holder exists
    data = request.json
    data['holder_id'] = holder_id
    
    new_claim = Claim(**data)
    db.session.add(new_claim)
    db.session.commit()
    return jsonify({"message": "Claim created", "claim_id": new_claim.claim_id}), 201
    
# --- GIS / GeoJSON Endpoint (Very Important! 🗺️) ---
@bp.route("/claims/geojson", methods=["GET"])
def get_claims_as_geojson():
    """
    Returns all claims with valid geometries as a GeoJSON FeatureCollection.
    This is what the frontend map (Leaflet/Mapbox) will use.
    """
    claims_with_geo = db.session.query(
        Claim.claim_id,
        Claim.claim_type,
        Claim.claim_status,
        Holder.first_name,
        ST_AsGeoJSON(Claim.claim_geometry).label('geometry')
    ).join(Holder).filter(Claim.claim_geometry.isnot(None)).all()

    features = []
    for claim in claims_with_geo:
        feature = {
            "type": "Feature",
            "geometry": json.loads(claim.geometry),
            "properties": {
                "claim_id": claim.claim_id,
                "claim_type": claim.claim_type,
                "status": claim.claim_status,
                "holder_name": claim.first_name
            }
        }
        features.append(feature)


@bp.route("/db-check", methods=["GET"])
def db_check():
    try:
        # Use text() for raw SQL
        result = db.session.execute(text("SELECT version();")).fetchone()
        postgis = db.session.execute(text("SELECT postgis_full_version();")).fetchone()
        return jsonify({
            "status": "connected",
            "postgres_version": result[0],
            "postgis_version": postgis[0]
        })
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)})


    return jsonify({
        "type": "FeatureCollection",
        "features": features
    })