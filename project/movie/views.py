from flask import render_template, Blueprint, redirect, url_for, request
from project.models import *
from project import db
from project.film import Film
from flask_login import current_user
import datetime

movie_blueprint = Blueprint(
    'movie', __name__,
    template_folder = 'templates'
)

@movie_blueprint.route('/movie/<string:id>', methods=['GET', 'POST'])
def movie(id):
    movie = Film(Movie.query.filter_by(title=id).first())
    localSystem = BoxOffice.query.first()
    error=None
    if request.method == 'POST':
        studio = Studio.query.filter_by(user=current_user.name).first()
        if request.form['submit_button'] == 'Change date':
            date = request.form['release_date']
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            weekday = date.weekday()
            if weekday == 4:
                db.session.add(DateChange(movie.title, studio.name, localSystem.currentDate, movie.release_date, date))
                db.session.commit()
                movie.release_date = date
                movie.update(localSystem.currentDate)
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
            return redirect(url_for('studio.studio'))

    return render_template("movie.html", user=current_user, movie=movie, error=error)