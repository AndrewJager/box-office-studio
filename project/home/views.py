from flask import render_template, Blueprint
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
    data = {}
    data['news'] = db.session.query(Announcement).all()
    data['changes'] = db.session.query(MovieChange).all()
    data['dateChanges'] = db.session.query(DateChange).all()
    data['boxOffice'] = Results.query.filter_by(date=(localSystem.currentDate - datetime.timedelta(days=1))).order_by(Results.movie_gross.desc()).all()
    return render_template("index.html", user=current_user, system=localSystem, data=data)

