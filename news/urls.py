from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewSet, CommentViewSet, UpvoteView

posts = PostViewSet.as_view({"get": "list", "post": "create"})
post_detail = PostViewSet.as_view({"put": "update", "delete": "destroy"})
comments = CommentViewSet.as_view({"get": "list", "post": "create"})
comment_detail = CommentViewSet.as_view({"put": "update", "delete": "destroy"})

urlpatterns = format_suffix_patterns(
    [
        path("posts/", posts),
        path("post/<int:pk>/", post_detail),
        path("comments/", comments),
        path("comment/<int:pk>/", comment_detail),
        path("post/upvote/<int:pk>/", UpvoteView.as_view()),
    ]
)
