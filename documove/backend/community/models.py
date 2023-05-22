from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Keyword(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    title = models.CharField(max_length=50)
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    rank = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Rate(models.Model):
#     review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='rates')
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rates')
#     score = models.IntegerField(validators= [
#         MaxValueValidator(10),
#         MinValueValidator(1)
#     ])

class Donation(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='donations')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='donations')
    points = models.IntegerField()
    keywords = models.ManyToManyField(Keyword, relatedName='community')

    def get_environment_keywords(self):
        return settings.ENVIRONMENT_KEYWORDS


    def update_donation_info(self):
        self.points = self.users.count()  
        self.save()
