from src.models.orm import db
from pony.orm import Optional, Required, PrimaryKey


class User_Password(db.Entity):
    id = PrimaryKey(int, auto=True)
    owner = Optional('User')
    hash = Required(str)
