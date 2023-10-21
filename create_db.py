from app import db, app
from views.events.models import Events
from views.users.model import User

with app.app_context():
    print("Creating database tables ...")
    db.create_all()
