from django.db import models
from django.contrib.auth.models import AbstractUser


class AccountUser(AbstractUser):

    age = models.IntegerField(
        blank=True,
        null=True,
    )

    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to='accounts',
    )

    def __str__(self):
        return self.username
