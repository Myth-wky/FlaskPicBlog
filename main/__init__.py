"""
 @Author: 19336
 @Email: 1933658780@qq.com
 @FileName: __init__.py.py
 @DateTime: 2024/1/9 13:43
 @SoftWare: PyCharm
 @comment:
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = 'MYTHWKY'
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql+pymysql://root:xxx@IP:3306/FlaskPicBlog'
                                             '?connect_timeout=3600')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = SECRET_KEY
    db.init_app(app)
    return app
