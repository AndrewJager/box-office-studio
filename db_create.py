from app import db
from models import *

db.create_all()

db.session.add(Announcement("Hello", "First post here"))

db.session.commit()