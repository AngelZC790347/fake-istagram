from wtforms import StringField, PasswordField, SubmitField
from .common import CommonForm


class RegistrationForm(CommonForm):
    confirm = PasswordField('Repeat Password', render_kw={"placeholder": "Confirm Password"})
    user_name = StringField('User Name', render_kw={"placeholder": "Username"})
    submit = SubmitField("Sig In")
