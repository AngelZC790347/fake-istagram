from flask import Blueprint, request, render_template, redirect, g, session
from src.models.form import registration, login
from src.models.orm.user import User
from src.models.orm.password import User_Password
from pony.orm import select
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/<mode>', methods=['GET', 'POST'])
def register(mode: str):
    redirect_message = ""
    if mode == "register":
        form = registration.RegistrationForm(request.form)
        if request.method == "POST" and form.validate():
            print(form.user_name.data, form.email.data)
            User(user_name=form.user_name.data, email=form.email.data, password=User_Password(hash=form.password.data))
            return "Your register was successfull go to <a href='/auth/login'>Log In<a/>"
    elif mode == 'login':
        form = login.LoginForm(request.form)
        redirect_message = 'Click aqui para <a href="/auth/register">registrarse<a/>'
        if request.method == "POST":
            current_user = select(u for u in User if u.email == form.email.data and u.password.hash == form.password.data).first()
            if current_user is not None:
                session['user_id'] = current_user.id
                return redirect('/')
    else:
        return ("", 404)

    return render_template("form.html", form=form, redirect_message=redirect_message)


@bp.get('logout')
def logout():
    session.clear()
    return redirect('login')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.current_user = None
    else:
        g.current_user = User.get(id=session["user_id"])
