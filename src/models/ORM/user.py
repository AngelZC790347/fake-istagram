from pony.orm import Required, Optional, Set, PrimaryKey
from src.models.orm import db


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    user_name = Required(str)
    email = Required(str)
    password = Optional('User_Password', cascade_delete=True)
    posts = Set("Post")
    followers = Set("User")
    followed = Set("User")

    def __dict__(self):
        return {
            "user_name": self.user_name,
            "email": self.email,
            # "posts": self.posts,
        }
