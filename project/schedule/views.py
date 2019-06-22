from flask import render_template, Blueprint
from flask_login import current_user
import datetime
from project.models import *
from project import db

schedule_blueprint = Blueprint(
    'schedule', __name__,
    template_folder = 'templates'
)

class SumResults:
    def __init__(self, name):
        self.name = name
        self.total = 0

    def addTotal(self, amount):
        self.total += amount

    def getGross(self):
        return self.total

    def getTitle(self):
        return self.name



@schedule_blueprint.route('/schedule')
def schedule():
    movies = {}
    localSystem = BoxOffice.query.first()
    curDate = localSystem.currentDate
    i = 0
    while i < 4:
        weekEnd = (curDate + datetime.timedelta(days=i*7)) + datetime.timedelta(days=6)
        movies[i] = db.session.query(Movie).filter(Movie.release_date >= (curDate + datetime.timedelta(days=i*7))).filter(Movie.release_date <= weekEnd).all()
        i = i + 1
        
    return render_template("schedule.html", user=current_user, system=localSystem, movies=movies, datetime=datetime, offset=0)

@schedule_blueprint.route('/schedule/<string:offset>')
def schedules(offset):
    movies = {}
    localSystem = BoxOffice.query.first()
    curDate = localSystem.currentDate
    i = 0
    while i < 4:
        weekEnd = ((curDate + datetime.timedelta(days=i*7)) +datetime.timedelta(days=int(offset))) + datetime.timedelta(days=6)
        movies[i] = db.session.query(Movie).filter(Movie.release_date >= (curDate + datetime.timedelta(days=int(offset))) + datetime
        .timedelta(days=i*7)).filter(Movie.release_date <= weekEnd).all()
        i = i + 1
        
    return render_template("schedule.html", user=current_user, system=localSystem, movies=movies, datetime=datetime, offset=int(offset))

@schedule_blueprint.route('/boxoffice/daily')
def boxoffice():
    localSystem = BoxOffice.query.first()
    date = localSystem.currentDate - datetime.timedelta(days=1)
    data = {}
    data['results'] = Results.query.filter_by(date=date).order_by(Results.movie_gross.desc()).all()
    data['type'] = 'daily'
    data['results_arr'] = []
    data['titles'] = []
    data['date'] = date
    for i in data['results']:
        data['results_arr'].append(i.movie_gross)
        data['titles'].append(i.movie)
    
    return render_template("boxoffice.html", user=current_user, system=localSystem, data=data, offset=0)

@schedule_blueprint.route('/boxoffice/daily/<string:offset>')
def boxoffices(offset):
    localSystem = BoxOffice.query.first()
    date = ((localSystem.currentDate -datetime.timedelta(days=1)) + datetime.timedelta(days=int(offset)))
    data = {}
    data['results'] = Results.query.filter_by(date=date).order_by(Results.movie_gross.desc()).all()
    data['type'] = 'daily'
    data['results_arr'] = []
    data['titles'] = []
    data['date'] = date
    for i in data['results']:
        data['results_arr'].append(i.movie_gross)
        data['titles'].append(i.movie)


    return render_template("boxoffice.html", user=current_user, system=localSystem, data=data, offset=int(offset))

@schedule_blueprint.route('/boxoffice/weekend')
def boxofficeweekend():
    localSystem = BoxOffice.query.first()
    date = localSystem.currentDate - datetime.timedelta(days=1)
    data = {}
    data['results'] = Results.query.filter(Results.date.between((date-datetime.timedelta(days=2)), date)).order_by(Results.movie_gross.desc()).all()
    data['type'] = 'weekend'
    data['results_arr'] = []
    data['titles'] = []
    data['date'] = date
    
    totals = {}
    for i in data['results']:
        data['day'] = i.date.weekday()
        if not i.movie in totals:
            total = SumResults(str(i.movie))
            totals[i.movie] = total
        totals[i.movie].addTotal(i.movie_gross)
    
    for i in totals:
        data['results_arr'].append(totals[i].getGross())
        data['titles'].append(totals[i].getTitle())
    
    return render_template("boxoffice.html", user=current_user, system=localSystem, data=data, offset=0)

@schedule_blueprint.route('/boxoffice/weekend/<string:offset>')
def boxofficeweekends(offset):
    localSystem = BoxOffice.query.first()
    date = (localSystem.currentDate - datetime.timedelta(days=1) + datetime.timedelta(days=int(offset) * 7))
    data = {}
    data['results'] = Results.query.filter(Results.date.between((date-datetime.timedelta(days=2)), date)).order_by(Results.movie_gross.desc()).all()
    data['type'] = 'weekend'
    data['results_arr'] = []
    data['titles'] = []
    data['date'] = date
    
    totals = {}
    for i in data['results']:
        data['day'] = i.date.weekday()
        if not i.movie in totals:
            total = SumResults(str(i.movie))
            totals[i.movie] = total
        totals[i.movie].addTotal(i.movie_gross)

    for i in totals:
        data['results_arr'].append(totals[i].getGross())
        data['titles'].append(totals[i].getTitle())
    
    return render_template("boxoffice.html", user=current_user, system=localSystem, data=data, offset=int(offset))

@schedule_blueprint.route('/boxoffice/weekly')
def boxofficeweekly():
    localSystem = BoxOffice.query.first()
    date = localSystem.currentDate - datetime.timedelta(days=1)
    data = {}
    data['results'] = Results.query.filter(Results.date.between((date-datetime.timedelta(days=6)), date)).order_by(Results.movie_gross.desc()).all()
    data['type'] = 'weekly'
    data['results_arr'] = []
    data['titles'] = []
    data['date'] = date
    
    totals = {}
    for i in data['results']:
        data['day'] = i.date.weekday()
        if not i.movie in totals:
            total = SumResults(str(i.movie))
            totals[i.movie] = total
        totals[i.movie].addTotal(i.movie_gross)
    
    for i in totals:
        data['results_arr'].append(totals[i].getGross())
        data['titles'].append(totals[i].getTitle())
    
    return render_template("boxoffice.html", user=current_user, system=localSystem, data=data, offset=0)

@schedule_blueprint.route('/boxoffice/weekly/<string:offset>')
def boxofficeweeklys(offset):
    localSystem = BoxOffice.query.first()
    date = (localSystem.currentDate - datetime.timedelta(days=1) + datetime.timedelta(days=int(offset) * 7))
    data = {}
    data['results'] = Results.query.filter(Results.date.between((date-datetime.timedelta(days=6)), date)).order_by(Results.movie_gross.desc()).all()
    data['type'] = 'weekly'
    data['results_arr'] = []
    data['titles'] = []
    data['date'] = date
    
    totals = {}
    for i in data['results']:
        data['day'] = i.date.weekday()
        if not i.movie in totals:
            total = SumResults(str(i.movie))
            totals[i.movie] = total
        totals[i.movie].addTotal(i.movie_gross)

    for i in totals:
        data['results_arr'].append(totals[i].getGross())
        data['titles'].append(totals[i].getTitle())
    
    return render_template("boxoffice.html", user=current_user, system=localSystem, data=data, offset=int(offset))