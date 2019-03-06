from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
import datetime

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
bcryptObj = Bcrypt(app)
localSystem = None

db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)