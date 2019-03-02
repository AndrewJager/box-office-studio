# sandbox for database stuff

from app import db
from models import *

db.session.add(Studio("Starandsnow studios", "admin", 150))

db.session.add(BoxOffice('2019-3-1'))

db.session.commit()