# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 23:44
# @author  : slark
# @File    : __init__.py
# @Software: PyCharm

from flask import Blueprint

main = Blueprint('main', __name__)
from app.models import Permission

from . import views, errors

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)