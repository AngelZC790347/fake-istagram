from wtforms import Form, EmailField, StringField


class RegistrationForm(Form):
    email = EmailField('Email Address')
    user_name = StringField("Usermame")
    password = StringField('password')
