# sandbox for database stuff

from project import db
from project.models import *

db.session.query(User).delete()
db.session.commit()

db.session.add(User("Starandsnow", "C-plus-plus"))
db.session.add(User("Batman", "password"))

db.session.commit()