# sandbox for database stuff

from project import db
from project.models import *

movies = db.session.query(Movie).all()
for m in movies:
    m.trailers = 0


db.session.commit()