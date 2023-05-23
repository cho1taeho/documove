from django.conf import settings
from django.db import models

class Theme(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    points = models.IntegerField()

class Giving(models.Model):
    id = models.IntegerField(primary_key=True)
    organization = models.JSONField()
    active = models.BooleanField()
    title = models.CharField(max_length=500)
    summary = models.TextField()
    contactName = models.CharField(max_length=200)
    contactAddress = models.CharField(max_length=200)
    contactCity = models.CharField(max_length=200)
    contactState = models.CharField(max_length=200)
    contactPostal = models.CharField(max_length=200)
    contactCountry = models.CharField(max_length=200)
    contactUrl = models.URLField()
    projectLink = models.URLField()
    progressReportLink = models.URLField()
    themeName = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    iso3166CountryCode = models.CharField(max_length=10)
    region = models.CharField(max_length=200)
    goal = models.FloatField()
    funding = models.FloatField()
    remaining = models.FloatField()
    numberOfDonations = models.IntegerField()
    status = models.CharField(max_length=200)
    need = models.TextField()
    longTermImpact = models.TextField()
    activities = models.TextField()
    additionalDocumentation = models.URLField()
    imageLink = models.URLField()
    imageGallerySize = models.IntegerField()
    videos = models.JSONField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    approvedDate = models.DateTimeField()
    donationOptions = models.JSONField()
    modifiedDate = models.DateTimeField()
    numberOfReports = models.IntegerField()
    dateOfMostRecentReport = models.DateTimeField()
    themes = models.JSONField()
    image = models.JSONField()
    countries = models.TextField()
    type = models.CharField(max_length=200)


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

