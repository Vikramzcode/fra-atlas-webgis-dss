import os

class Config:
    # PostgreSQL + PostGIS connection via environment variables
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}"
        f":{os.getenv('DB_PASS')}"
        f"@{os.getenv('DB_HOST', 'localhost')}"
        f":{os.getenv('DB_PORT', 5432)}"
        f"/{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")  # keep for Flask sessions
