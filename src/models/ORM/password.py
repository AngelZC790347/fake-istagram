from ...models import db
from pony.orm import Required


class UserPassword(db.Entity):
    owner = Required('User', cascade_delete=True)
    hash = Required(str)
