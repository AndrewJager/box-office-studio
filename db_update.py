# sandbox for database stuff

from project import db
from project.models import *

db.session.query(User).delete()
db.session.commit()

db.session.add(User("Starandsnow", "email@gmail.com", "Starandsnow Studios", "C-plus-plus"))
db.session.add(User("Batman", "email@gmail.com", "None", "password"))

db.session.commit()