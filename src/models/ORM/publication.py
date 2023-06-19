from pony.orm import Required
from ...models import db


class Post(db.Entity):
    description = Required(str)
    owner = Required("User", cascade_delete=True)
    likes = Required(int)
