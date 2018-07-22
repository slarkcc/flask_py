# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 23:45
# @author  : slark
# @File    : views.py
# @Software: PyCharm

from . import main
from app.models import *
from flask import abort, render_template

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)

