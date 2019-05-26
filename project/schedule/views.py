from flask import render_template, Blueprint
from flask_login import current_user
import datetime
from project.models import *


schedule_blueprint = Blueprint(
    'schedule', __name__,
    template_folder = 'templates'
)

@schedule_blueprint.route('/schedule')
def schedule():
    movies = {}
    localSystem = BoxOffice.query.first()
    i = 0
    while i < 4:
        movies[i] = Movie.query.filter_by(release_date=(localSystem.currentDate + datetime.timedelta(days=i*7))).all()
        i = i + 1
        
    return render_template("schedule.html", user=current_user, system=localSystem, movies=movies, datetime=datetime, offset=0)

@schedule_blueprint.route('/schedule/<string:offset>')
def schedules(offset):
    movies = {}
    localSystem = BoxOffice.query.first()
    i = 0
    while i < 4:
        movies[i] = Movie.query.filter_by(release_date=((localSystem.currentDate + datetime.timedelta(days=int(offset))) + datetime.timedelta(days=i*7))).all()
        i = i + 1
        
    return render_template("schedule.html", user=current_user, system=localSystem, movies=movies, datetime=datetime, offset=int(offset))

@schedule_blueprint.route('/boxoffice')
def boxoffice():
    localSystem = BoxOffice.query.first()
    results = Results.query.filter_by(date=localSystem.currentDate - datetime.timedelta(days=7)).all()
    return render_template("boxoffice.html", user=current_user, system=localSystem, results=results, offset=0)

@schedule_blueprint.route('/boxoffice/<string:offset>')
def boxoffices(offset):
    localSystem = BoxOffice.query.first()
    date = (localSystem.currentDate + datetime.timedelta(days=int(offset))) - datetime.timedelta(days=7)
    results = Results.query.filter_by(date=date).all()
    return render_template("boxoffice.html", user=current_user, system=localSystem, results=results, offset=int(offset))
