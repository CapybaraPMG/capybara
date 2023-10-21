from database import db
from utils import gen_uuid
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(250), primary_key=True, default=str(gen_uuid))
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    photo = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
