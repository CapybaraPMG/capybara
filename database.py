from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import settings
from app import app 

app = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = settings.MySQL_DATABASE_URL
