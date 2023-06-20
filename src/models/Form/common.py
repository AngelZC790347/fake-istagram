from wtforms import Form, EmailField, PasswordField


class CommonForm(Form):
    email = EmailField(label="Email", render_kw={"placeholder": "Email"})
    password = PasswordField(label="Password", render_kw={"placeholder": "Paswword"})
