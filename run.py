"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/4/12
  Time: 23:54
 """
from blog import create_app

__author__ = 'liujianhan'

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])
