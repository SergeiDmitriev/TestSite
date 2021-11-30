from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(verbose_name="Аватарка", blank=True, null=True)
    email = models.EmailField(verbose_name="email", unique=True)
