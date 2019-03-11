from flask import render_template, Blueprint, request
from project.models import *
from project import db
from flask_login import current_user
import datetime
from project.film import Film

admin_blueprint = Blueprint(
    'admin', __name__,
    template_folder = 'templates'
)

@admin_blueprint.route('/admin', methods=['GET', 'POST'])
def admin():
    localSystem = BoxOffice.query.first()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Next week':
            
            # calc box office for current date
            # store box office
            # change date - done
            nextDay = localSystem.currentDate + datetime.timedelta(days=7)
            localSystem.currentDate = nextDay

            # remove old announcemnts/changes
            # update movies
            movies = db.session.query(Movie).all()
            for movie in movies:
                film = Film(movie)
                film.update(localSystem.currentDate)
            # create announcments

            db.session.commit()

    return render_template('admin.html', user=current_user, system=localSystem)