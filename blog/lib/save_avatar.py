"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/4/24
  Time: 0:25
 """
__author__ = 'liujianhan'

import os
import secrets
from tkinter import Image

from flask import current_app

__author__ = 'liujianhan'


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn
