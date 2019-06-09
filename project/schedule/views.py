from flask import render_template, Blueprint
from flask_login import current_user
import datetime
from project.models import *
from project import db

schedule_blueprint = Blueprint(
    'schedule', __name__,
    template_folder = 'templates'
)

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
        #movies[i] = Movie.query.filter_by(release_date=((localSystem.currentDate + datetime.timedelta(days=int(offset))) + datetime.timedelta(days=i*7))).all()
        i = i + 1
        
    return render_template("schedule.html", user=current_user, system=localSystem, movies=movies, datetime=datetime, offset=int(offset))

@schedule_blueprint.route('/boxoffice')
def boxoffice():
    localSystem = BoxOffice.query.first()
    results = Results.query.filter_by(date=localSystem.currentDate).all()

    return render_template("boxoffice.html", user=current_user, system=localSystem, results=results, offset=0)

@schedule_blueprint.route('/boxoffice/<string:offset>')
def boxoffices(offset):
    localSystem = BoxOffice.query.first()
    date = (localSystem.currentDate + datetime.timedelta(days=int(offset)))
    results = Results.query.filter_by(date=date).all()
    return render_template("boxoffice.html", user=current_user, system=localSystem, results=results, offset=int(offset))
