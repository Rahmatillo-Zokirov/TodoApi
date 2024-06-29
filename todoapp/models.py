from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
