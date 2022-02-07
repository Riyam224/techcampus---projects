from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# ! models == tables in database


class Board(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)

# ! to convert the queryset to string
    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=200)
    created_by = models.ForeignKey(
        User, related_name='topics', on_delete=models.CASCADE)
    board = models.ForeignKey(
        Board, related_name='topics', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(
        Topic, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
