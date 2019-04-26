"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/4/13
  Time: 0:05
 """
from flask import Blueprint

from blog.models import Permission

__author__ = 'liujianhan'

main = Blueprint('main', __name__)

from . import errors, views


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
