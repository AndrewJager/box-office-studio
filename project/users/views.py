from flask import flash, redirect, render_template, request, \
   url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user, logged_in
from project.users.form import LoginForm, RegisterForm
from project.models import User, bcryptObj, Studio
from project import db

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None and bcryptObj.check_password_hash(user.password, request.form['password']):
                #session['logged_in'] = True
                login_user(user)
                flash('You were logged in.')
                return redirect(url_for('home.home'))
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', user=current_user, logged_in=logged_in, form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.welcome'))


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.username.data,
            email=form.email.data,
            studio=form.username.data + " studios",
            password=form.password.data
        )
        studio = Studio(name=user.name + " studios", user=user.name, cash=150)
        db.session.add(user)
        db.session.add(studio)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.home'))
    return render_template('register.html', user=current_user, logged_in=logged_in, form=form)