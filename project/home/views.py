from flask import render_template, redirect, url_for, \
     request, session, flash, Blueprint
from flask_bcrypt import Bcrypt
from flask_login import login_required, current_user
import datetime
from project import app, db, localSystem
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


@home_blueprint.route('/welcome')
def welcome():
    localSystem = BoxOffice.query.first()
    return render_template("welcome.html")
