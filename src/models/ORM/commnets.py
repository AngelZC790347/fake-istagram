from pony.orm import Required, Set
from src.models.orm import db


class Comment(db.Entity):
    post_origin = Required("Post")
    user_owner = Required("User")
    responses = Set("Comment", reverse="responses")
