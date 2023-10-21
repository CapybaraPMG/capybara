from database import db
from utils import gen_uuid
from datetime import datetime
from sqlalchemy.orm import relationship


class Events(db.Model):
    __tablename__ = "events"
    id = db.Column(db.String(80), primary_key=True, default=str(gen_uuid))
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    date_time = db.Column(db.String(250), nullable=False)
    venue = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    is_charged = db.Column(db.Boolean, nullable=False)
    poster = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.String(250), db.ForeignKey("users.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = relationship("User", back_populates="events")