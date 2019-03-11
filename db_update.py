# sandbox for database stuff

from project import db
from project.models import *

users = db.session.query(User).first()
users.isAdmin = True


db.session.commit()