from flask import render_template, Blueprint, redirect, url_for, request
from project.models import *
from project import db
from project.film import Film
from flask_login import current_user
import datetime
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

movie_blueprint = Blueprint(
    'movie', __name__,
    template_folder = 'templates'
)

@movie_blueprint.route('/movie/<string:id>', methods=['GET', 'POST'])
def movie(id):
    movie = Film(Movie.query.filter_by(title=id).first())
    localSystem = BoxOffice.query.first()
    user = current_user
    error=None
    if request.method == 'POST':
        if request.form['submit_button'] == 'Change date':
            date = request.form['release_date']
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            weekday = date.weekday()
            if weekday == 4:
                db.session.add(DateChange(movie.title, user.studio, localSystem.currentDate, movie.release_date, date))
                movie.release_date = date
                movie.updateDB()
                db.session.commit()
            else:
                error="Movie must be released on a friday"
        elif request.form['submit_button'] == 'Change poster':
            file_to_upload = request.files['poster']
            if file_to_upload:
                poster = upload(file_to_upload, width=200, height=350, crop="limit")
                movie.poster = poster['url']
                movie.updateDB()
                db.session.merge(movie.movie)
                db.session.commit()
                
        elif request.form['submit_button'] == 'Release trailer':
            pass # do something else
        elif request.form['submit_button'] == 'Cancel movie':
            movie = movie.movie
            user.cash = user.cash + (movie.budget - movie.budget_spent)
            db.session.add(MovieChange(movie.title, user.studio, localSystem.currentDate, False))
            db.session.delete(movie)
            db.session.commit()
            return redirect(url_for('studio.studio'))

    return render_template("movie.html", user=current_user, movie=movie, error=error, system=localSystem)