from flask import Flask, jsonify
from .config import Config
from .database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize DB
    db.init_app(app)

    # Import and register API routes
    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    # ✅ Root route
    @app.route("/")
    def index():
        return jsonify({"message": "FRA Atlas API is running 🚀", "docs": "/api"})

    # ✅ Database check route
    @app.route("/db-check")
    def db_check():
        try:
            result = db.session.execute("SELECT version();").fetchone()
            postgis = db.session.execute("SELECT postgis_full_version();").fetchone()
            return jsonify({
                "status": "connected",
                "postgres_version": result[0],
                "postgis_version": postgis[0]
            })
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

    return app

