# sandbox for database stuff

from project import db
from project.models import *

box = db.session.query(BoxOffice).first()
box.scifi_demand = 5
box.fantasy_demand = 5
box.drama_demand = 5
box.horror_demand = 5
box.comedy_demand = 5
box.war_demand = 5
box.superhero_demand = 5
box.action_demand = 5


db.session.commit()