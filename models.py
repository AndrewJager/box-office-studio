from app import db 

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Announcement(db.Model):

    __tablename__ = "announcements"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    genre = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    budget_spent = db.Column(db.Integer, nullable=False)
    advertising = db.Column(db.Integer, nullable=False)
    advertising_spent = db.Column(db.Integer, nullable=False)
    poster = db.Column(db.String)
    dom_gross = db.Column(db.String, nullable=False)
    int_gross = db.Column(db.String, nullable=False)
    china_gross = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date, nullable=True)
    production_date = db.Column(db.Date, nullable=True)

    def __init__(self, title, genre, budget):
        self.title = title
        self.genre = genre
        self.status = "Pre-production"
        self.budget = budget
        self.budget_spent = 0
        self.advertising = 0
        self.advertising_spent = 0
        self.poster = ""
        self.dom_gross = 0
        self.int_gross = 0
        self.china_gross = 0
        self.release_date = None
        self.production_date = "2019-3-1"
