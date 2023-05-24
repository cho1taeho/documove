from django.conf import settings
from django.db import models

class Theme(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)


class Giving(models.Model):
    active = models.BooleanField(null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    themeName = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    funding = models.FloatField(null=True)
    remaining = models.FloatField(null=True)
    numberOfDonations = models.IntegerField(null=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    activities = models.TextField(null=True, blank=True)
    imageLink = models.CharField(max_length=255, null=True, blank=True)
    imageGallerySize = models.IntegerField(null=True)
    approvedDate = models.DateTimeField(null=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=50)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')



class Movie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    genre_ids = models.ManyToManyField(Genre, related_name='movies')  # genre_ids 필드를 Genre 모델과 연결합니다.

    poster_path = models.CharField(max_length=200, blank=True, null=True)
    adult = models.BooleanField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    original_title = models.CharField(max_length=100)
    original_language = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    popularity = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    theme_id = models.CharField(max_length=50)

