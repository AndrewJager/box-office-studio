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
            return render_template("studio.html", system=localSystem, movies=movies, studio=studio, error=error)
        else:
            return redirect(url_for('home.home'))
            
    else:
        movies = Movie.query.filter_by(studio=studio.name).all()
        return render_template("studio.html", system=localSystem, movies=movies, studio=studio)