# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 23:44
# @author  : slark
# @File    : tests.py
# @Software: PyCharm

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()