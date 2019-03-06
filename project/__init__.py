from flask import Flask, g
from flask_sqlalchemy  import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import datetime

app = Flask(__name__)
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

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(schedule_blueprint)
app.register_blueprint(movie_blueprint)

from project.models import User

login_manager.login_view = "users.login"

@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter(User.id == int(user_id)).first()
    return user