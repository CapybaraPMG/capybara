from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import settings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.MySQL_DATABASE_URL
db = SQLAlchemy(app)