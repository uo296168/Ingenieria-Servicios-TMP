from flask import Blueprint

health = Blueprint("health", __name__)

from app.health import views