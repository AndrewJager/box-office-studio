# sandbox for database stuff

from project import db
from project.models import *

sections = db.session.query(ForumSection).all()
for i in sections:
    db.session.delete(i)

db.session.commit()