from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager()
login_manager.init_app(app)
app.config.from_object(os.environ['APP_SETTINGS'])
bcryptObj = Bcrypt(app)
localSystem = None

db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint
from project.schedule.views import schedule_blueprint
from project.movie.views import movie_blueprint
from project.studio.views import studio_blueprint
from project.admin.views import admin_blueprint
from project.forum.views import forum_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(schedule_blueprint)
app.register_blueprint(movie_blueprint)
app.register_blueprint(studio_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(forum_blueprint)

from project.models import User

login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
    try:
        user = User.query.filter(User.id == int(user_id)).first()
    except:
        user = None
    return user