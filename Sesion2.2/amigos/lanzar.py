import os
from app import create_app

modo = os.getenv("DEPLOYMENT_MODE", "production")

app = create_app(modo)