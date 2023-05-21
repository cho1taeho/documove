from django.db import models
from django.conf import settings

# Create your models here.
class Theme(models.Model):
    theme_point = models.ManyToManyField(Point, related_name='theme_point')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')

    
    moviepk = models.IntegerField()
    subject = models.TextField()
    theme_sum_point = models.IntegerField()
    theme_countPeople = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Movie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    theme_ids = models.ManyToManyField(Theme)

    movie_name = models.CharField(max_length=150)
    movie_desc = models.TextField()
    movie_class  = models.TextField()
    movie_playtime = models.IntegerField()
    movie_director = models.CharField(max_length=150)
    movie_participant = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Point(models.Model):
    subject = models.TextField()
    theme_point = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
