from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Comment, Review, Donation, TopDonator

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
        # 원래는 그냥 user 객체를 보여줘야 하는데, 장고 내부적으로 할 때에는 그 처리를 해 주지 않아도 username을 보여줬었다.
        # 하지만 serializer는 user를 그냥 보여준다고 할 때, 그냥 db의 pk값을 보여주는게 맞다.
        # 해결 방법 1. ReviewSerializer의 depth를 1로 줘서. 더 파고 들어갈 depth가 있을 때에만 더 들어간다.
        fields = '__all__'
        depth = 1
        read_only_fields = ('user', 'like_users',)

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