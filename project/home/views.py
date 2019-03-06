from flask import render_template, redirect, url_for, \
     request, session, flash, Blueprint
from flask_bcrypt import Bcrypt
from flask_login import login_required, current_user
import datetime
from project import app, db, localSystem
from project.film import Film
from project.models import *


home_blueprint = Blueprint(
    'home', __name__,
    template_folder = 'templates'
)

@home_blueprint.route('/')
def home():
    localSystem = BoxOffice.query.first()
    news = db.session.query(Announcement).all()
    changes = db.session.query(MovieChange).all()
    dateChanges = db.session.query(DateChange).all()
    return render_template("index.html", news=news, moviechanges=changes, dateChanges=dateChanges)

@home_blueprint.route('/studio', methods={'GET', 'POST'})
@login_required
def studio():
    error = None
    localSystem = BoxOffice.query.first()
    studio = Studio.query.filter_by(user=current_user.name).first()
    if request.method == "POST":
        if 'title' in request.form:
            canAdd = Movie.query.filter_by(title=request.form['title']).first()
            if canAdd is None:
                studio.cash = studio.cash - int(request.form['budget'])
                db.session.add(MovieChange(request.form['title'], studio.name, localSystem.currentDate, True))
                db.session.add(Movie(request.form['title'], studio.name, request.form['genre'], request.form['budget']))
                db.session.commit()
            else:
                error="A movie with that title exists"
            movies = Movie.query.filter_by(studio=studio.name).all()
            return render_template("studio.html", system=localSystem, movies=movies, studio=studio, session=session, error=error)
        else:
            return redirect(url_for('home'))
            
    else:
        movies = Movie.query.filter_by(studio=studio.name).all()
        return render_template("studio.html", system=localSystem, movies=movies, studio=studio, session=session)

@home_blueprint.route('/schedule')
def schedule():
    movies = {}
    localSystem = BoxOffice.query.first()
    i = 0
    while i < 4:
        movies[i] = Movie.query.filter_by(release_date=(localSystem.currentDate + datetime.timedelta(days=i*7))).all()
        i = i + 1
        
    return render_template("schedule.html", system=localSystem, movies=movies, datetime=datetime, offset=0)

@home_blueprint.route('/schedule/<int:offset>')
def schedules(offset):
    movies = {}
    localSystem = BoxOffice.query.first()
    i = 0
    while i < 4:
        movies[i] = Movie.query.filter_by(release_date=((localSystem.currentDate + datetime.timedelta(days=offset)) + datetime.timedelta(days=i*7))).all()
        i = i + 1
        
    return render_template("schedule.html", system=localSystem, movies=movies, datetime=datetime, offset=offset)

@home_blueprint.route('/movie/<string:id>', methods=['GET', 'POST'])
def movie(id):
    movie = Film(Movie.query.filter_by(title=id).first())
    studio = Studio.query.filter_by(user=current_user.name).first()
    localSystem = BoxOffice.query.first()
    error=None
    if request.method == 'POST':
        if request.form['submit_button'] == 'Change date':
            date = request.form['release_date']
            weekday = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
            if weekday == 4:
                db.session.add(DateChange(movie.title, studio.name, "2019-3-1", movie.release_date, date))
                db.session.commit()
                movie.release_date = date
                movie.update()
                db.session.commit()
            else:
                error="Movie must be released on a friday"
        elif request.form['submit_button'] == 'Release trailer':
            pass # do something else
        elif request.form['submit_button'] == 'Cancel movie':
            movie = movie.movie
            studio.cash = studio.cash + (movie.budget - movie.budget_spent)
            db.session.add(MovieChange(movie.title, studio.name, localSystem.currentDate, False))
            db.session.delete(movie)
            db.session.commit()
            return redirect(url_for('studio'))
        return render_template("movie.html", movie=movie, error=error)
    else:
        return render_template("movie.html", movie=movie, error=error)

@home_blueprint.route('/welcome')
def welcome():
    localSystem = BoxOffice.query.first()
    return render_template("welcome.html")
