from flask import Blueprint, request, render_template
from models.Form.registration import RegistrationForm
bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        pass
    return render_template("register.html", form=form)
