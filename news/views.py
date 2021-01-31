from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().annotate(count_votes=Count("upvotes"))
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpvoteView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        try:
            post = get_object_or_404(Post, id=pk)

            if post.upvotes.filter(id=self.request.user.id).exists():
                post.upvotes.remove(self.request.user)
                return Response({"message": "Unvoted successfully"})

            post.upvotes.add(self.request.user)
            return Response({"message": "Upvoted successfully"})

        except Http404:
            return Response({"message": "Post does not exist"})
