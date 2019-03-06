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
    news = db.session.query(Announcement).all()
    changes = db.session.query(MovieChange).all()
    dateChanges = db.session.query(DateChange).all()
    return render_template("index.html", user=current_user, news=news, moviechanges=changes, dateChanges=dateChanges)

