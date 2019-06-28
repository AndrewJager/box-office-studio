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
    if request.method == "POST":
        if 'title' in request.form:
            canAdd = Movie.query.filter_by(title=request.form['title']).first()
            if canAdd is None: 
                if request.form['budget'] != '' and int(request.form['budget']) >= 1:
                    user.cash = user.cash - int(request.form['budget'])
                    db.session.add(MovieChange(request.form['title'], user.studio, localSystem.currentDate, True))
                    db.session.add(Movie(request.form['title'], user.studio, request.form['genre'], request.form['budget'], localSystem.currentDate))
                    db.session.commit()
                else:
                    error="Movie budget must be at least one"
            else:
                error="A movie with that title exists"

    movies = {}
    movies[0] = Movie.query.filter_by(studio=user.studio).filter(Movie.release_date > localSystem.currentDate).order_by(Movie.release_date).all()
    movies[1] = Movie.query.filter_by(studio=user.studio).filter(Movie.release_date <= localSystem.currentDate).order_by(Movie.release_date).all()
    movies[2] = Movie.query.filter_by(studio=user.studio).filter_by(release_date = None).order_by(Movie.release_date).all()
    return render_template("studio.html", user=current_user, system=localSystem, movies=movies, error=error)