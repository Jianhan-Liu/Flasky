"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/4/14
  Time: 1:01
 """
__author__ = 'liujianhan'

from flask import Blueprint

auth = Blueprint('auth', __name__)
from . import views