from main import create_app
from flask import render_template
from main.model import PostPic, Picture
from main import db
from flask import request
from PIL import Image
import os


UPLOAD_FOLDER = './static/image/'
THUMBNAILS_FOLDER = './static/thumbnails/'

app = create_app()


# 主页
@app.route('/', methods=['GET', 'POST'])
def index():
    all_img = Picture.query.all()
    img_show = [{'id': img.id, 'title': img.title, 'path': img.thumbnails} for img in all_img]
    return render_template('index.html', img_show=img_show)


# 上传图片（隐藏URL）
# 将上传的图片保存到本地，然后将图片的路径保存到数据库中
@app.route('/post', methods=['GET', 'POST'])
def upload():
    form = PostPic()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        pic = form.pic.data
        time = form.time.data
        print(request.files)
        # 保存原始图片到本地
        if 'pic' in request.files:
            pic_file = request.files['pic']
            pic_file.save(os.path.join(UPLOAD_FOLDER, pic_file.filename))
            print('原始图片上传成功')
        # 保存缩略图到本地
            im = Image.open(os.path.join(UPLOAD_FOLDER, pic_file.filename))
            im.thumbnail((500, 500))
            im.save(os.path.join(THUMBNAILS_FOLDER, pic_file.filename))
            print('缩略图上传成功')
        # 保存图片路径到数据库
        picture = Picture(title=title, description=description,
                          src="image/" + request.files['pic'].filename,
                          thumbnails="thumbnails/" + request.files['pic'].filename, time=time)
        db.session.add(picture)
        try:
            db.session.commit()
            print('保存成功')
        except Exception as e:
            print(e)
            db.session.rollback()
            print('保存失败')
        return render_template('index.html')
    return render_template('post.html', form=form)


# # 个人主页
# @app.route('/user', methods=['GET', 'POST'])
# def user():
#     return render_template('author.html')


# 图片细节
@app.route('/detail/<title>?<id>', methods=['GET', 'POST'])
def detail(title, id):
    img_detail = Picture.query.filter_by(id=id).first()
    return render_template('detail.html', img_detail=img_detail)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
