from django.db import models
from django.contrib.auth.models import AbstractUser

class Worker(AbstractUser):
    position = models.ForeignKey(
        "Position",
        on_delete=models.PROTECT,
        related_name="workers",
    )
