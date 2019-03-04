# sandbox for database stuff

from app import db
from models import *

db.session.add(User("Starandsnow", "C-plus-plus"))
db.session.add(User("admin", "admin"))

db.session.commit()