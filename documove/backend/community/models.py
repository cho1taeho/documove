from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie, Giving
class Keyword(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')

    
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    review = models.BooleanField(null=True, blank=True)
    
    # title = models.CharField(max_length=50)
    # movie_title = models.CharField(max_length=50)
    # content = models.TextField()
    # rank = models.FloatField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)





class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Moviepoint(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='points_users')
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='points_movies')
    # obtained_at = models.DateTimeField(null=True, blank=True)
    # class Meta:
    #     constraints  = [
    #         models.UniqueConstraint(
    #             fields = ['users', 'movies']
    #             name = 'users-movies composite key'
    #         )
    #     ]

class GivingDonation(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donation_user')
    givings = models.ForeignKey(Giving, on_delete=models.CASCADE, related_name='donation_giving')
    giving_points = models.IntegerField()


class Donation(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='donation_review')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='donation_users')
    points = models.IntegerField()
    keywords = models.ManyToManyField(Keyword, related_name='donation_keywords')

    def get_environment_keywords(self):
        return settings.ENVIRONMENT_KEYWORDS


    def update_donation_info(self):
        self.points = self.users.count()  
        self.save()

class TopDonator(models.Model):
    donation = models.OneToOneField(Donation, on_delete=models.CASCADE, related_name='top_donator')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @classmethod
    def update_top_donator(cls):
        top_donation = Donation.objects.order_by('-points').first()
        if top_donation:
            top_donator = top_donation.users.order_by('-points').first()
            if top_donator:
                top_donator_instance, created = cls.objects.get_or_create(donation=top_donation)
                top_donator_instance.user = top_donator
                top_donator_instance.save()