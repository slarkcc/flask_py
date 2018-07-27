# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 23:45
# @author  : slark
# @File    : forms.py
# @Software: PyCharm

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Length, Email, data_required, Regexp, ValidationError
from app.models import *


class LoginForm(Form):
    email = StringField('Email', validators=[data_required(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[data_required()])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField("log in")


class EditProfileForm(Form):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')


class EditProfileAdminForm(Form):
    email = StringField('Email', validators=[data_required(), Length(1, 64), Email()])
    username = StringField('username', validators=[data_required(),
                                                   Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                          0,
                                                          'Usernames must have only letters numbers dots or underscores'
                                                          )
                                                   ]
                           )
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already registered.")

    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(field.data).first():
            raise ValidationError("Username already in use.")
