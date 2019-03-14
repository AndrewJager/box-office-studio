from flask import render_template, Blueprint, url_for, redirect, request
from project.models import *
from flask_login import login_required, current_user
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import os

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
    poster= None
    if request.method == "POST":
        if 'title' in request.form:
            canAdd = Movie.query.filter_by(title=request.form['title']).first()
            if canAdd is None:
                file_to_upload = request.files['file']
                if file_to_upload:
                    poster = upload(file_to_upload, width=100, height=200, crop="limit")
                user.cash = user.cash - int(request.form['budget'])
                db.session.add(MovieChange(request.form['title'], user.studio, localSystem.currentDate, True))
                db.session.add(Movie(request.form['title'], user.studio, request.form['genre'], request.form['budget'], localSystem.currentDate))
                db.session.commit()
            else:
                error="A movie with that title exists"
            movies = Movie.query.filter_by(studio=user.studio).all()
            return render_template("studio.html", user=current_user, system=localSystem, movies=movies, error=error, poster=poster)
        else:
            return redirect(url_for('home.home'))
            
    else:
        movies = Movie.query.filter_by(studio=user.studio).all()
        return render_template("studio.html", user=current_user, system=localSystem, movies=movies , poster=poster)