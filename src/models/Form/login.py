from .common import CommonForm
from wtforms import SubmitField


class LoginForm(CommonForm):
    submit = SubmitField("Log in")
