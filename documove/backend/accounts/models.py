from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Create def to resolve HINT: Use a callable instead, e.g., use `dict` instead of `{}`?
def genre_default():
    return {'12': 0, '14': 0, '16': 0, '18': 0, '27': 0, '28': 0, '35': 0, '36': 0, '37': 0, '53':0, '80': 0, '99':0, '878':0, '9648':0, '10402':0, '10749':0, '10751':0, '10752':0, '10770':0 }

class Keyword(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(AbstractUser):
    genre_dict = models.JSONField(default=genre_default)
    point = models.IntegerField(default = 0)
    badge = models.ImageField(upload_to='badges/', blank=True, null=True)
    keywords = models.ManyToManyField(Keyword, related_name='accountuser')

    def get_environment_keywords(self):
        return settings.ENVIRONMENT_KEYWORDS
    

    # default 값이 이거라서 변하는게 없는 것.
    def __str__(self):
        return self.username



class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    movies = models.ManyToManyField('movies.Movie', related_name='wishlists')
    created_at = models.DateTimeField(auto_now= True)
    keywords = models.ManyToManyField(Keyword, related_name='wishlist')

    def get_environment_keywords(self):
        return settings.ENVIRONMENT_KEYWORDS
