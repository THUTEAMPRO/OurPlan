from flask import session, url_for, render_template, request
from werkzeug.utils import redirect
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from model import User
# from routes.util import app
from server import get_db, get_app
from flask_login import login_user, login_required, logout_user, current_user

from . import auth
from forms import LoginForm, RegistrationForm

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What is your email?', validators=[Required()])
    submit = SubmitField('Submit')


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    form = LoginForm(csrf_enabled=False)
    if(current_user.is_authenticated):
        logout_user()
        return redirect('/auth/login')
    else:
        return redirect('/auth/login')
    
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if(current_user.is_authenticated):
        return redirect("/home");
    else:
        form = LoginForm(csrf_enabled=False)
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user, form.remember_me.data)
                return redirect(request.args.get('next') or "/home")
            print('Invalid email or password.')
        return render_template('auth/login.html', form=form)
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         user = User.query.filter_by(username=form.name.data).first()
#         if user is None:
#             db = get_db()
#             db.create_all()
#             user_tmp = User(username=name)
#             db.session.add(user_tmp)
#             session['known'] = False
#         else:
#             session['known'] = True
#         session['name'] = name
#         return redirect(url_for('register'))
#     return render_template('register.html', form=form, name=session.get('name'),
#                            known=session.get('known', False))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(csrf_enabled=False)
    if form.validate_on_submit():
        username = form.username.data
        emails = form.email.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is None:
            db = get_db()
            user_tmp = User(username=username, email=emails)
            user_tmp.password=password
            db.session.add(user_tmp)
            db.session.commit()
            login_user(user_tmp)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = username
        session['email'] = emails
        return redirect('/home')
    else:
        return render_template("register.html", form=form)
    #return render_template('register.html', form=form, name=session.get('name'), email=session.get('email'), known=session.get('known', False))
