from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='User')
    task = models.CharField(max_length=200, verbose_name='Task')
    completed = models.BooleanField(default=False, verbose_name='Completed')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At")
    completed_at = models.DateTimeField(
        auto_now_add=False, null=True, verbose_name=("Completed At"))

    def save(self, *args, **kwargs):
        if self.completed and not self.completed_at:
            self.completed_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.task
