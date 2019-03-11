from project import db
from project.models import *


BoxOffice.query.delete()
db.session.add(BoxOffice("2019-3-1"))
DateChange.query.delete()
Movie.query.delete()
MovieChange.query.delete()

db.session.commit()