from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='images', null=True)
    date_of_birth = models.CharField(max_length=150, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True,
        choices=(
        ('man', 'мужчина'),
        ('women', 'женщина')
    ))
    brief_information = models.TextField(blank=True, null=True)