# -*- coding:utf-8 -*-
# $File: example.py
# $Author: cz <chenze-321n[at]163[dot]com>
from flask import session, url_for

from api.auth.views import NameForm
from util import *
from model import User
from flask.ext.mail import Mail, Message


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/example")
def example():
    """ example for get method """
    return "args: " + str(request.args)


@app.route("/example/<test>")
def example_url(test):
    """ example for url args """
    return "args: " + str(test)


@app.route("/example_post", methods=["POST"])
def example_post():
    """ examle for post method """
    return "data:(" + request.data + ")" + "form:(" + str(request.form) + ")"


@app.route("/example_render")
def example_render():
    """ examle for jinja2 render """
    return render_template("example.html", content="args example")


#
def send_email(to, subject, template, **kwargs):
    mail = Mail(app)
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


@app.route('/email', methods=['GET', 'POST'])
def email():
    return render_template('email.html')
"""
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            pass
        else:
            send_email("huashiyiqike@qq.com", 'New User',
                       'mail/new_user', user=user)
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('register.html', form=form, name=session.get('name'),
                           known=session.get('known', False))
"""
