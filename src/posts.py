from flask import Blueprint, request, render_template, g, redirect
from src.models.form.publication_post import PostPhotoForm
from src.middlewares import login_required
from src.models.orm.publication import Post
bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('/', methods=["GET", "POST"])
@login_required
def post():
    form = PostPhotoForm()
    if request.method == "POST" and form.validate_on_submit():
        print(form.description.data)
        Post(description=form.description.data, owner=g.current_user, photo=request.files['photo'].stream.read(), likes=0)
        return redirect('/')
    return render_template("mypage.html", form=form)
