from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


# Create your models here.
# Create def to resolve HINT: Use a callable instead, e.g., use `dict` instead of `{}`?
def genre_default():
    return {'12': 0, '14': 0, '16': 0, '18': 0, '27': 0, '28': 0, '35': 0, '36': 0, '37': 0, '53':0, '80': 0, '99':0, '878':0, '9648':0, '10402':0, '10749':0, '10751':0, '10752':0, '10770':0 }



class User(AbstractUser):
    genre_dict = models.JSONField(default=genre_default)
    points = models.IntegerField(default = 0)
    badge = models.ImageField(upload_to='badges/', blank=True, null=True)
   
    def add_points(self, points):
        self.points += points
        self.save()

    def subtract_points(self, points):
        if self.points - points < 0:
            raise ValidationError('후원 포인트가 모자랍니다.')
        else:
            self.points -= points
        self.save()

    def get_environment_keywords(self):
        return settings.ENVIRONMENT_KEYWORDS
    


    def __str__(self):
        return self.username



class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    movies = models.ManyToManyField('movies.Movie', related_name='wishlists')
    created_at = models.DateTimeField(auto_now= True)
    

    def add_movie(self, movie):
        self.movies.add(movie)

    def remove_movie(self, movie):
        self.movies.remove(movie)


    
    def __str__(self):
        return f'Wishlist by {self.user.username}'