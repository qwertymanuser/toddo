from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField(
        max_length=255,
    )
    completed = models.BooleanField(
        default=False
    )
    created = models.DateField(
        auto_now_add=True
    )
    id = models.AutoField(primary_key=True)