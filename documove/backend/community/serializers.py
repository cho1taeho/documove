from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Comment, Review, Donation, TopDonator, Moviepoint

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at')
        # read_only_fields = ('review',)



# class RateSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Rate
#         fields = '__all__'
#         read_only_fields = ('movie', 'user',)

# TODO : 안쓰는 시리얼라이저
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user',)

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review      
        fields = '__all__'
        read_only_fields = ('user', 'movie')

class PointSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Moviepoint
        fields = '__all__'
        read_only_fields = ('users', 'movies')



class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'
        

class TopDonatorSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    total_donation = serializers.SerializerMethodField()
    user_count = serializers.SerializerMethodField()

    class Meta:
        model = TopDonator
        fields = ('username', 'total_donation', 'user_count')

    def get_username(self, obj):
        return obj.user.username

    def get_total_donation(self, obj):
        return obj.donation.points

    def get_user_count(self, obj):
        return obj.donation.users.count()

class DonationSerializer(serializers.ModelSerializer):
    top_donator = TopDonatorSerializer(read_only=True)

    class Meta:
        model = Donation
        fields = ('id', 'review', 'users', 'points', 'keywords', 'top_donator')