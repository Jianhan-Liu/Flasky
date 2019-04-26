"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/4/13
  Time: 22:07
 """
from threading import Thread

from flask import current_app, render_template

from blog import mail

__author__ = 'liujianhan'

from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
