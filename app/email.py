# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 23:42
# @author  : slark
# @File    : email.py
# @Software: PyCharm

from manage import app
from flask_mail import Message
from flask import render_template
from . import mail

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config["FLASKY_MAIL_SUBJECT_PREFIX"] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=[to])

    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
