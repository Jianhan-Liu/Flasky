"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/4/15
  Time: 1:32
 """
from functools import wraps
from flask import abort

from flask_login import current_user

from blog.models import Permission

__author__ = 'liujianhan'


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
