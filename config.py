# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 23:43
# @author  : slark
# @File    : config.py
# @Software: PyCharm

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "my_secret"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = "[Flasky]"
    FLASKY_MAIL_SENDER = "cg110692@163.com"
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    # MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_USERNAME = "cg110692@163.com"
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_PASSWORD = "Cg112992"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}