from database import db
from utils import gen_uuid
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(80), primary_key=True, default=str(gen_uuid))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.string(120), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    events = db.relationship("Events", backref="events", lazy=True)
