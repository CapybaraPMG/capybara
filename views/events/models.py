from database import db
from utils import gen_uuid
from datetime import datetime


class Events(db.Model):
    __tablename__ = "events"
    id = db.Column(db.String(80), primary_key=True, default=str(gen_uuid))
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    date_time = db.Column(db.String(250), nullable=False)
    venue= db.Column(db.string(120), nullable=False)
    price = db.Columgn(db.Integer,nullable=False)
    is_charged=db.Column(db.Boolean, nullable=False)
    poster = db.Column(db.String(250), nullable=False)
    user_id = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user= db.relationship("User", back_populates="businesses", primaryjoin="foreign(Event.user_id) == User.id")
