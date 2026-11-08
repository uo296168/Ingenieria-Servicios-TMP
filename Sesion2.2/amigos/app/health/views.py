from app.health import health
from app import db
from sqlalchemy import text

@health.route("/health")
def health_check():
    try:
        db.session.execute(text("SELECT 1")) 
        return {"status": "ok", "database": "ok"}, 200
    except Exception:
        return {"status": "error", "database": "error"}, 503