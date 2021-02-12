from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    '''This is the CustomUser model with a new field "age"'''
    age = models.PositiveIntegerField(null=True, blank=True)
