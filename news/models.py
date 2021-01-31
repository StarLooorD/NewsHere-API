from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    link = models.CharField(max_length=200, null=False)
    creation_date = models.DateField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name="vote", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} (by {self.author})"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.post} ({self.author}): {self.content}"
