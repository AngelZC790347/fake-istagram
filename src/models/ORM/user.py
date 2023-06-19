from pony.orm import Required, Optional, Set
from ...models import db


class User(db.Entity):
    user_name = Required(str)
    email = Required(str)
    password = Optional("UserPassword", cascade_delete=True)
    posts = Set("Post")
    followers = Set("User")
    followed = Set("User")
