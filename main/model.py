"""
 @Author: 19336
 @Email: 1933658780@qq.com
 @FileName: model.py
 @DateTime: 2024/1/9 14:13
 @SoftWare: PyCharm
 @comment: 数据库模型和表单类
"""
from main import db
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired


class PostPic(FlaskForm):
    title = StringField('标题', validators=[DataRequired()])
    description = TextAreaField('描述', validators=[DataRequired()])
    pic = FileField('图片', validators=[DataRequired()])
    time = DateField('时间', validators=[DataRequired()])
    submit = SubmitField('上传')


class Picture(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    src = db.Column(db.String(255), nullable=False)
    thumbnails = db.Column(db.String(255), nullable=False)
    time = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Picture %r>' % self.title
