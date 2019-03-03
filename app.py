from flask import Flask, render_template, redirect, url_for, \
     request, session, flash
from flask_sqlalchemy  import SQLAlchemy
from functools import wraps
import os
import datetime
from film import Film

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)
from models import *

localSystem = None

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    localSystem = BoxOffice.query.first()
    news = db.session.query(Announcement).all()
    return render_template("index.html", news=news)

@app.route('/studio', methods={'GET', 'POST'})
@login_required
def studio():
    localSystem = BoxOffice.query.first()
    studio = Studio.query.filter_by(user='admin').first()
    if request.method == "POST":
        if 'title' in request.form:
            canAdd = Movie.query.filter_by(title=request.form['title']).first()
            if canAdd is None:
                db.session.add(Movie(request.form['title'], "admin", request.form['genre'], request.form['budget']))
                db.session.commit()
            movies = Movie.query.filter_by(studio='admin').all()
            return render_template("studio.html", system=localSystem, movies=movies, studio=studio, session=session)
        else:
            return redirect(url_for('home'))
            
    else:
        movies = Movie.query.filter_by(studio='admin').all()
        return render_template("studio.html", system=localSystem, movies=movies, studio=studio, session=session)

@app.route('/schedule')
def schedule():
    movies = {}
    localSystem = BoxOffice.query.first()
    i = 0
    while i < 8:
        movies[i] = Movie.query.filter_by(release_date=(localSystem.currentDate + datetime.timedelta(days=i*7))).all()
        i = i + 1
        
    return render_template("schedule.html", system=localSystem, movies=movies, datetime=datetime)

@app.route('/movie/<string:id>', methods=['GET', 'POST'])
def movie(id):
    movie = Film(Movie.query.filter_by(title=id).first())
    error=None
    if request.method == 'POST':
        if request.form['submit_button'] == 'Change date':
            date = request.form['release_date']
            weekday = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
            if weekday == 4:
                movie.release_date = date
                movie.update()
                db.session.commit()
            else:
                error="Movie must be released on a friday"
        elif request.form['submit_button'] == 'Do Something Else':
            pass # do something else
        return render_template("movie.html", movie=movie, error=error)
    else:
        return render_template("movie.html", movie=movie, error=error)

@app.route('/welcome')
def welcome():
    localSystem = BoxOffice.query.first()
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid login'
        else:
            session['logged_in'] = True
            flash('Logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for("welcome"))


if __name__ == '__main__':
    app.run(debug=True)