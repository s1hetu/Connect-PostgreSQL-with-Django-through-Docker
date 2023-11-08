from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class DummyModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.description}"
