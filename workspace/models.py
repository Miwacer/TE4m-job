from django.db import models
from django.contrib.auth.models import AbstractUser

class Position(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(
        "Position",
        on_delete=models.PROTECT,
        related_name="workers",
        null = True,
    )



class Task(models.Model):
    STATUS = (
        ("UR", "Urgent"),
        ("HI", "High"),
        ("MD", "Medium"),
        ("LW", "Low")
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    priority = models.CharField(max_length=2, choices=STATUS)
    task_type = models.ForeignKey(TaskType, on_delete=models.PROTECT)
    assignees = models.ManyToManyField(
        'Worker',
        related_name="assignees",
    )
