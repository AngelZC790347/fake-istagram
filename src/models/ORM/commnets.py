from pony.orm import Required, Set
from ...models import db


class Comment(db.Entity):
    post_origin = Required("Post", cascade_delete=True)
    user_owner = Required("User")
    responses = Set("Comment", reverse="responses")
