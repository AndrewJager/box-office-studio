# sandbox for database stuff

from app import db
from models import *

db.session.add(Studio("Starandsnow", "admin", 150))

db.session.commit()