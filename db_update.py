# sandbox for database stuff

from project import db
from project.models import *

db.session.add(Studio("Starandsnow", "admin", 150))
db.session.add(BoxOffice("2019-3-1"))

db.session.commit()