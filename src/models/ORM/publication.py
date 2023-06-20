from pony.orm import Required
from src.models.orm import db
import base64


class Post(db.Entity):
    description = Required(str)
    owner = Required("User")
    photo = Required(bytes)
    likes = Required(int)

    def get_img_src(self):
        return f"data:image/png;base64,{base64.b64encode(self.photo).decode()}"
