from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import settings
from app import app

db_app = SQLAlchemy(app)
db_app.config["SQLALCHEMY_DATABASE_URI"] = settings.MySQL_DATABASE_URL
