from flask import flash, redirect, render_template, request, \
   url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from project.users.form import LoginForm, RegisterForm
from project.models import User, bcryptObj, BoxOffice, Movie
from project import db

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    localSystem = BoxOffice.query.first()
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcryptObj.check_password_hash(user.password, request.form['password']):
                login_user(user)
                flash('You were logged in.')
                return redirect(url_for('home.home'))
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', system=localSystem, user=current_user, form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.home'))


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    localSystem = BoxOffice.query.first()
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            studio=form.username.data + " studios",
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', system=localSystem, user=current_user, form=form)

@users_blueprint.route('/user', methods=['GET', 'POST'])
def user():
    localSystem = BoxOffice.query.first()
    thisUser = current_user
    movies = {}
    movies[0] = Movie.query.filter_by(studio=thisUser.studio).filter(Movie.release_date > localSystem.currentDate).order_by(Movie.release_date).all()
    movies[1] = Movie.query.filter_by(studio=thisUser.studio).filter(Movie.release_date <= localSystem.currentDate).order_by(Movie.release_date).all()
    movies[2] = Movie.query.filter_by(studio=thisUser.studio).filter_by(release_date = None).order_by(Movie.release_date).all()
    confirm = False
    if request.method == 'POST':
        confirm = userPost(confirm, thisUser)

    return render_template('user.html', system=localSystem, user=current_user, thisUser=thisUser, confirm=confirm, movies=movies)

@users_blueprint.route('/user/<string:id>', methods=['GET', 'POST'])
def specificUser(id):
    localSystem = BoxOffice.query.first()
    thisUser = User.query.filter_by(name=id).first()
    movies = {}
    movies[0] = Movie.query.filter_by(studio=thisUser.studio).filter(Movie.release_date > localSystem.currentDate).order_by(Movie.release_date).all()
    movies[1] = Movie.query.filter_by(studio=thisUser.studio).filter(Movie.release_date <= localSystem.currentDate).order_by(Movie.release_date).all()
    movies[2] = Movie.query.filter_by(studio=thisUser.studio).filter_by(release_date = None).order_by(Movie.release_date).all()
    confirm = False
    if request.method == 'POST':
        confirm = userPost(confirm, thisUser)

    return render_template('user.html', system=localSystem, user=current_user, thisUser=thisUser, confirm=confirm, movies=movies)

def userPost(confirm, thisUser):
    if request.form['submit_button'] == 'Change password':
        pass

    if request.form['submit_button'] == 'Delete account':
        confirm = True

    if request.form['submit_button'] == 'Delete user':
        confirm = True

    if request.form['submit_button'] == 'Confirm':
        db.session.delete(thisUser)
        db.session.commit()

    return confirm