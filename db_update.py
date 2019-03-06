# sandbox for database stuff

from project import db
from project.models import *

db.session.query(User).delete()
db.session.query(Studio).delete()
db.session.query(Movie).delete()
db.session.query(DateChange).delete()
db.session.query(MovieChange).delete()
db.session.commit()


db.session.commit()