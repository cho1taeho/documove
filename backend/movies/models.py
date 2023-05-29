from django.conf import settings
from django.db import models

class Theme(models.Model):
    pass

class Giving(models.Model):
    id = models.IntegerField(primary_key=True)
    organization = models.JSONField(null=True, blank=True, default=dict)
    active = models.BooleanField()
    title = models.CharField(max_length=256)
    summary = models.TextField()
    themeName = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    funding = models.FloatField()
    remaining = models.FloatField()
    numberOfDonations = models.IntegerField()
    status = models.CharField(max_length=64)
    activities = models.TextField()
    imageLink = models.URLField()
    imageGallerySize = models.IntegerField(null=True, blank=True)
    videos = models.JSONField(null=True, blank=True, default=list)
    approvedDate = models.DateTimeField()
    themes = models.JSONField()
    image = models.JSONField()
    type = models.CharField(max_length=64)

class Genre(models.Model):
    name = models.CharField(max_length=50)



class Movie(models.Model):
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

