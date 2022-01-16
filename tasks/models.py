import django
from django.db import models

import datetime


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    # avatar = models.ImageField(upload_to='', max_length=100)

    def __str__(self):
        return f"<User id={self.id} username={self.username} password={self.password} />"


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=django.utils.timezone.now())

    def __str__(self):
        return f"<Task user={self.user} title={self.title} description={self.description} create_at={self.create_at} deadline={self.deadline} />"
