import base64
from flask import Flask, render_template, g
from .config import flask_config
from pony.flask import Pony
from src.models import *
from src.models.orm import *
from src.models.orm.password import User_Password
from src.models.orm.publication import Post
from src.models.shared import user
from flask_bootstrap import Bootstrap4
from src.middlewares import login_required
# from flask_wtf import CSRFProtect
from src.auth import bp as auth_bp
from src.posts import bp as post_bp
# basico configuration
app = Flask(__name__, static_url_path="", static_folder="/static")
app.config.update(flask_config)
app.static_folder = "static/"
db.bind(**flask_config['PONNY'])
db.generate_mapping(create_tables=True)
Pony(app)
Bootstrap4(app)
# CSRFProtect(app)

# register Modules
app.register_blueprint(auth_bp)
app.register_blueprint(post_bp)


@app.get('/')
@login_required
def index():
    return render_template("mypage.html", usuario=g.current_user)
