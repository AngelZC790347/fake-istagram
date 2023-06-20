from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import SubmitField, FileField, StringField


class PostPhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])
    description = StringField("description", render_kw={"placeholder": "Set some description for your post"})
    submit = SubmitField('Post Photo')
