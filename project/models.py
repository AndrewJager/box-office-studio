from project import db, bcryptObj
import bcrypt

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
    studio = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    budget_spent = db.Column(db.Integer, nullable=False)
    advertising = db.Column(db.Integer, nullable=False)
    advertising_spent = db.Column(db.Integer, nullable=False)
    dom_gross = db.Column(db.String, nullable=False)
    int_gross = db.Column(db.String, nullable=False)
    china_gross = db.Column(db.String, nullable=False)
    release_date = db.Column(db.Date, nullable=True)
    production_date = db.Column(db.Date, nullable=True)
    poster = db.Column(db.String)

    def __init__(self, title, studio, genre, budget, curDate):
        self.title = title
        self.studio = studio
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
        self.production_date = curDate


class BoxOffice(db.Model):
    __tablename__ = "boxoffice"

    id = db.Column(db.Integer, primary_key=True)
    currentDate = db.Column(db.Date, nullable=False)
    scifi_demand = db.Column(db.Integer)
    fantasy_demand = db.Column(db.Integer)
    drama_demand = db.Column(db.Integer)
    horror_demand = db.Column(db.Integer)
    comedy_demand = db.Column(db.Integer)
    war_demand = db.Column(db.Integer)
    superhero_demand = db.Column(db.Integer)
    action_demand = db.Column(db.Integer)

    def __init__(self, curDate):
        self.currentDate = curDate


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    studio = db.Column(db.String, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)
    cash = db.Column(db.Float)

    def __init__(self, name, studio, password):
        self.name = name
        self.studio = studio
        self.cash = 150
        pwhash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        self.password = pwhash.decode('utf8')
        self.isAdmin = False
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class DateChange(db.Model):
    __tablename__ = "datechanges"
    
    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String, nullable=False)
    studio = db.Column(db.String, nullable=False)
    dateOfChange = db.Column(db.Date, nullable=False)
    oldDate = db.Column(db.Date)
    newDate = db.Column(db.Date, nullable=False)

    def __init__(self, movie, studio, dateOfChange, oldDate, newDate):
        self.movie = movie
        self.studio = studio
        self.dateOfChange = dateOfChange
        self.oldDate = oldDate
        self.newDate = newDate


class MovieChange(db.Model):
    __tablename__ = "moviechanges"

    id = db.Column(db.Integer, primary_key=True)
    movie = db.Column(db.String, nullable=False)
    studio = db.Column(db.String, nullable=False)
    dateOfChange = db.Column(db.Date, nullable=False)
    created = db.Column(db.Boolean, nullable=False)

    def __init__(self, movie, studio, dateOfChange, created):
        self.movie = movie
        self.studio = studio
        self.dateOfChange = dateOfChange
        self.created = created


class Results(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    movie_1 = db.Column(db.String)
    movie_1_results = db.Column(db.Float)
    movie_2 = db.Column(db.String)
    movie_2_results = db.Column(db.Float)
    movie_3 = db.Column(db.String)
    movie_3_results = db.Column(db.Float)
    movie_4 = db.Column(db.String)
    movie_4_results = db.Column(db.Float)
    movie_5 = db.Column(db.String)
    movie_5_results = db.Column(db.Float)
    movie_6 = db.Column(db.String)
    movie_6_results = db.Column(db.Float)
    movie_7 = db.Column(db.String)
    movie_7_results = db.Column(db.Float)
    movie_8 = db.Column(db.String)
    movie_8_results = db.Column(db.Float)
    movie_9 = db.Column(db.String)
    movie_9_results = db.Column(db.Float)
    movie_10 = db.Column(db.String)
    movie_10_results = db.Column(db.Float)
    movie_11 = db.Column(db.String)
    movie_11_results = db.Column(db.Float)
    movie_12 = db.Column(db.String)
    movie_12_results = db.Column(db.Float)
    movie_13 = db.Column(db.String)
    movie_13_results = db.Column(db.Float)
    movie_14 = db.Column(db.String)
    movie_14_results = db.Column(db.Float)
    movie_15 = db.Column(db.String)
    movie_15_results = db.Column(db.Float)
    movie_16 = db.Column(db.String)
    movie_16_results = db.Column(db.Float)
    movie_17 = db.Column(db.String)
    movie_17_results = db.Column(db.Float)
    movie_18 = db.Column(db.String)
    movie_18_results = db.Column(db.Float)
    movie_19 = db.Column(db.String)
    movie_19_results = db.Column(db.Float)
    movie_20 = db.Column(db.String)
    movie_20_results = db.Column(db.Float)
