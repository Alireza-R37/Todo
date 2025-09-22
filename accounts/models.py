# models.py
from django.conf import settings
from django.db import models

class Task(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    # ...

task = form.save(commit=False)
task.owner = request.user
task.save()