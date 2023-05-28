from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, WishlistSerializer
from django.shortcuts import get_object_or_404
from .models import User, Wishlist
from django.http import JsonResponse
from community.models import GivingDonation
from movies.models import Giving
from community.serializers import GivingDonationSerializer

# Create your views here.
@api_view(['POST'])
def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def subtract_points(request):
    user = get_object_or_404(User)
    
    point = request.data.get('point')
    givingId = request.data.get('givingId')
    print(givingId)
    foundGiving = get_object_or_404(Giving, id = givingId )
    user.subtract_points(point)
    
    newGivingDonation = GivingDonation.objects.create(users = user, givings = foundGiving, giving_points=point)
    
    print()
    # save
    user_serializer = UserSerializer(user, data=request.data)
    newGivingDonation.save()
    # giving_serializer = GivingDonationSerializer(newGivingDonation, data=request.data)
    # if giving_serializer.is_valid(raise_exception=True):
    #     giving_serializer.save()
    if user_serializer.is_valid(raise_exception=True):
        user_serializer.save()
   
    return Response(user_serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# def getThemePointList(request):

@api_view(['POST'])
def viewhistory(request):
    pass

@api_view(['GET'])
def mypage_view(request):
    user = get_object_or_404(User)
    wishlist = Wishlist.objects.filter(user=user)

    user_serializer = UserSerializer(user)
    wishlist_serializer = WishlistSerializer(wishlist, many=True)

    return JsonResponse({
        'user': user_serializer.data,
        'wishlist': wishlist_serializer.data,
    })
