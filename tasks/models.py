from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks',
        db_index=True,
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





#  models.ForeignKey(User, on_delete=models.CASCADE)  # مالک تسک