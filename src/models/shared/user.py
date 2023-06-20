class User(object):
    """docstring for User"""

    def __init__(self, user_name, posts, followers, followed):
        super(User, self).__init__()
        self.user_name = user_name
        self.posts = posts
        self.followers = followers
        self.followed = followed
