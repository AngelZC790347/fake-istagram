from flask import Flask
from config import flask_config
from pony.flask import Pony
from models import *
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from auth import bp as auth_bp
# basico configuration
app = Flask(__name__)
app.config.update(flask_config)
db.bind(**flask_config['PONNY'])
db.generate_mapping(create_tables=True)
Pony(app)
Bootstrap(app)
CSRFProtect(app)

# register Modules
app.register_blueprint(auth_bp)


@app.get('/')
def index():
    return "Inicio"
