import functools
from flask import g, redirect


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.current_user is None:
            return redirect('/auth/login')
        return view(**kwargs)

    return wrapped_view
