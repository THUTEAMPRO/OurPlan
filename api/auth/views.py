from flask import session, url_for, render_template
from werkzeug.utils import redirect
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from model import User
# from routes.util import app
from server import get_db, get_app

from . import auth
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What is your email?', validators=[Required()])
    submit = SubmitField('Submit')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
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
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        emails = form.email.data
        user = User.query.filter_by(username=name).first()
        if user is None:
            db = get_db()
            db.create_all()
            user_tmp = User(username=name, email=emails)
            db.session.add(user_tmp)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = name
        session['email'] = emails
        return redirect(url_for('register'))
    return render_template('register.html', form=form, name=session.get('name'),
                           email=session.get('email'),
                           known=session.get('known', False))