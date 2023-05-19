from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ViewHistory(models.Model):
    movie_durations = models.DurationField(null=True, blank=True) # 내가 영상을 본 시간 기록
    created_at = models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
    movie_wishlist = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now= True)


class Support(models.Model):
    username = models.CharField(max_length=150, blank= True)
    point = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

class movie(models.Model):
    moviepk = models.IntegerField()
    movie_name = models.CharField(max_length=150)
    movie_desc = models.TextField()
    movie_class  = models.TextField()
    movie_playtime = models.IntegerField()
    movie_director = models.CharField(max_length=150)
    movie_participant = models.CharField(max_length=155)

class Theme(models.Model):
    themepk = models.IntegerField()
    moviepk = models.IntegerField()
    subject = models.TextField()
    theme_sum_point = models.IntegerField()
    theme_countPeople = models.IntegerField()

class Point(models.Model):
    
    subject = models.TextField()
    theme_point = models.IntegerField()


