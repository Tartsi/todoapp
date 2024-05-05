from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='User')
    task = models.CharField(max_length=200, verbose_name='Task')
    completed = models.BooleanField(default=False, verbose_name='Completed')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.task
