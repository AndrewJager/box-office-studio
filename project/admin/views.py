from flask import render_template, Blueprint, request
from project.models import *
from project import db
from flask_login import current_user
import datetime
from cloudinary.uploader import destroy

admin_blueprint = Blueprint(
    'admin', __name__,
    template_folder = 'templates'
)

@admin_blueprint.route('/admin', methods=['GET', 'POST'])
def admin():
    localSystem = BoxOffice.query.first()
    users = User.query.all()
    movies = Movie.query.all()
    if request.method == 'POST':
        if request.form['submit_button'] == 'Next week':
            i = 0
            while i < 7: #update for every day of week
                # change date
                lastDay = localSystem.currentDate - datetime.timedelta(days=1)
                weekday = localSystem.currentDate.weekday()
                
                # update movies
                movies = db.session.query(Movie).all()
                for movie in movies:
                    lastDayGross = Results.query.filter_by(movie=movie.title, date=lastDay).first()
                    studio = User.query.filter_by(studio=movie.studio).first()
                    movie.update(localSystem.currentDate, lastDayGross, weekday)
                    if movie.status == "Released":
                        gross = movie.cur_gross
                        if gross > 0:
                            result = Results(localSystem.currentDate, movie.title, gross)
                            studio.cash = studio.cash + (gross * constants.STUDIO_CUT_USA)
                            db.session.add(result)

                i = i + 1
                localSystem.currentDate = localSystem.currentDate + datetime.timedelta(days=1)

            # remove old announcemnts/changes
            # create announcments

            db.session.commit()
        elif request.form['submit_button'] == 'Reset':
            BoxOffice.query.delete()
            db.session.add(BoxOffice("2019-3-1"))
            DateChange.query.delete()
            movies = Movie.query.all()
            for movie in movies:
                destroy('Box-Office-Studio/Posters/' + movie.title)
            Movie.query.delete()
            MovieChange.query.delete()
            Results.query.delete()
            for user in db.session.query(User).all():
                user.cash = 150

            db.session.commit()

    return render_template('admin.html', user=current_user, system=localSystem, users=users, movies=movies)