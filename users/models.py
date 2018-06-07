from django.db import models
from django.contrib.auth.models import AbstractUser
from contribution.models import Language


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    default_language = models.ForeignKey(Language, default=None, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.email