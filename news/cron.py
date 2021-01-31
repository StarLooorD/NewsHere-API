from .models import Post


def reset_upvotes():
    posts = Post.objects.all()
    for post in posts:
        post.upvotes.clear()
