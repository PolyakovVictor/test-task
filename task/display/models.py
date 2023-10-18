from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
