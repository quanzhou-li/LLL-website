from flask_wtf import Form
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(Form):
    content = TextAreaField('Comment', validators=[DataRequired()])
    picture = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')
