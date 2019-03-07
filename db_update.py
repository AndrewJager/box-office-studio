# sandbox for database stuff

from project import db
from project.models import *

users = db.session.query(User).all()
users.isAdmin = False


db.session.commit()