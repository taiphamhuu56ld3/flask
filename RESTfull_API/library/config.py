import os

# Components taken from .env
SECRET_KEY = os.environ.get("KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
# Notifications are not displayed when working with SQLALCHEMY
SQLALCHEMY_TRACK_MODIFICATIONS = False
