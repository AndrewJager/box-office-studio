from flask import render_template, Blueprint, url_for, redirect, request
from project.models import *
from flask_login import login_required, current_user

studio_blueprint = Blueprint(
    'studio', __name__,
    template_folder = 'templates'
)

@studio_blueprint.route('/studio', methods={'GET', 'POST'})
@login_required
def studio():
    error = None
    localSystem = BoxOffice.query.first()
    user = current_user
    upcomingMovies = Movie.query.filter_by(studio=user.studio).filter(Movie.release_date > localSystem.currentDate).order_by(Movie.release_date).all()
    releasedMovies = Movie.query.filter_by(studio=user.studio).filter(Movie.release_date <= localSystem.currentDate).order_by(Movie.release_date).all()
    undatedMovies = Movie.query.filter_by(studio=user.studio).filter_by(release_date = None).order_by(Movie.release_date).all()
    if request.method == "POST":
        if 'title' in request.form:
            canAdd = Movie.query.filter_by(title=request.form['title']).first()
            if canAdd is None:
                user.cash = user.cash - int(request.form['budget'])
                db.session.add(MovieChange(request.form['title'], user.studio, localSystem.currentDate, True))
                db.session.add(Movie(request.form['title'], user.studio, request.form['genre'], request.form['budget'], localSystem.currentDate))
                db.session.commit()
            else:
                error="A movie with that title exists"
            return render_template("studio.html", user=current_user, system=localSystem, upcomingMovies=upcomingMovies, releasedMovies=releasedMovies, undatedMovies=undatedMovies)
        else:
            return redirect(url_for('home.home'))
            
    else:
        return render_template("studio.html", user=current_user, system=localSystem, upcomingMovies=upcomingMovies, releasedMovies=releasedMovies, undatedMovies=undatedMovies)