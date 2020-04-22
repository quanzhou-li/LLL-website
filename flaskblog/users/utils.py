import os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail



def save_picture(form_picture):
    random_hex = os.urandom(8).hex()
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/pictures', picture_fn)

    output_size = (250,250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='quanzhou.li.cs@gmail.com', recipients=[user.email])
    msg.body = '''To reset your password, visit the following link:
{}

If you did not make this request then simply ignore this email and no change would apply.
    '''.format(url_for('users.reset_token', token=token, _external=True))
    mail.send(msg)
