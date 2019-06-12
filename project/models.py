from project import db, bcryptObj
import bcrypt
import datetime
import constants

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
    dom_gross = db.Column(db.Integer)
    int_gross = db.Column(db.Integer)
    china_gross = db.Column(db.Integer)
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
        self.poster = '/static/images/no-poster.png'

    def getScale(self):
        return round(((self.budget * self.getGenreScale(self.genre)) + 500) / 30)

    def getPreProEnd(self):
        return self.production_date + datetime.timedelta(days=self.getScale() * constants.PRE_PRODUCTION_LENGTH)

    def getFilmingEnd(self):
        return self.production_date + datetime.timedelta(days=self.getScale() * constants.FILMING_LENGTH)

    def getProductionEnd(self):
        return self.production_date + datetime.timedelta(days=self.getScale())

    def update(self, currentDate, lastGross, weekday):
        if self.status == "Pre-production":
            if currentDate > self.getPreProEnd():
                self.status = "Filming"
            
        if self.status == "Filming":
            if currentDate > self.getFilmingEnd():
                self.status = "Post-production"
            
        if self.status == "Post-production":
            if currentDate > self.getProductionEnd():
                self.status = "Finished"

        if self.status == "Finished":
            if self.release_date != None:
                if currentDate > self.release_date:
                    self.status = "Released"

        if self.status == "Released":
            hype = 10 #temp
            if lastGross is None: #opening
                self.cur_gross = (hype * self.getScale())
            else:
                if self.getWeekdayScale(weekday) != 0:
                    self.cur_gross = lastGross.movie_gross * self.getWeekdayScale(weekday)
                else:
                    self.cur_gross = lastGross.movie_gross / 1.2

            self.dom_gross += self.cur_gross
            if self.cur_gross < constants.MIN_GROSS_CUTOFF:
                self.status = "Closed"


    def getGenreScale(self, genre):
        if genre == "Sci-Fi":
            scale = 10
        elif genre == "Fantasy":
            scale = 8
        elif genre == "Drama":
            scale = 2
        elif genre == "Horror":
            scale = 4
        elif genre == "Comedy":
            scale = 3
        elif genre == "War":
            scale = 6
        elif genre == "Superhero":
            scale = 8
        elif genre == "Action":
            scale = 6

        return scale

    def getWeekdayScale(self, weekday):
        if weekday == 0:
            return constants.MONDAY_MODIFIER
        elif weekday == 1:
            return constants.TUESDAY_MODIFIER
        elif weekday == 3:
            return constants.WENDSDAY_MODIFIER
        elif weekday == 4:
            return constants.THURSDAY_MODIFIER
        else:
            return 0


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
    movie = db.Column(db.String)
    movie_gross = db.Column(db.Float)

    def __init__(self, date, movie, gross):
        self.date = date
        self.movie = movie
        self.movie_gross = gross
