"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/4/13
  Time: 14:40
 """
__author__ = 'liujianhan'

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@main.app_errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500


@main.app_errorhandler(403)
def page_forbidden(e):
    return render_template('errors/403.html'), 403
