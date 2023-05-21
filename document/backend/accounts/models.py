from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    points = models.IntegerField(default = 0)
    badge = models.ImageField(upload_to='badges/', blank=True, null= True)


class ViewHistory(models.Model):
    movie_durations = models.DurationField(null=True, blank=True) # 내가 영상을 본 시간 기록
    created_at = models.DateTimeField(auto_now=True)


class Wishlist(models.Model):
    movie_wishlist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now= True)