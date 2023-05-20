from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    points = models.IntegerField(default = 0)
    badge = models.ImageField(upload_to='badges/', blank=True, null= True)
    