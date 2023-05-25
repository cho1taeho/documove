import random
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Movie, Genre, Giving
from .serializers import MovieDetailSerializer,MovieSerializer, MovieRandomSerializer, GenreSerializer,GivingSerializer
from community.models import GivingDonation

from django.conf import settings

from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

import json

# user 모델 가져오기
from django.contrib.auth import get_user_model

# giving api 가져오기


@api_view(['GET'])
def movie_detail(request, pk):
    # try:
    #     movie = Movie.objects.get(pk=pk)
    # except Movie.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
        
    # serializer = MovieDetailSerializer(movie)
    movie = Movie.objects.get(pk=pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def giving(request):
    if request.method == 'GET':
        givings = Giving.objects.all()
        
        serializer = GivingSerializer(givings, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = GivingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def totalPointByTheme(request):
    totalPointTheme = dict()
    themes = settings.ENVIRONMENT_KEYWORDS
    for t in themes:
        totalPointTheme[t] = 0
    
    donation = GivingDonation.objects.all()
    for d in donation:
        totalPointTheme[d.givings.themes['theme'][0]['id']] += d.giving_points
    
    return Response(json.dumps(totalPointByTheme), status=status.HTTP_200_OK)


@api_view(['GET'])
def movies(request):
    # if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieDetailSerializer(movies, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
# 인기순으로 영화 제목 보내기 (selectBox)
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def home(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        random_movies = random.sample(list(movies), 50)
        serializer = MovieSerializer(random_movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 영화 상세 데이터
# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def movie_detail(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = MovieDetailSerializer(movie)
#     return Response(serializer.data)

# tinder에 보낼 랜덤 영화
# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def random(request):
#     movies = Movie.objects.order_by('?')[:200]
#     serializer = MovieRandomSerializer(movies, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# GET : genre 데이터를 리턴
# POST : tinder로 받아온 선호 장르 입력
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def genres(request):
    person = get_object_or_404(get_user_model(), username=request.user)
    # 해당 유저가 어떤 장르를 가장 좋아하는지 체크하기 위한 Json(dict type)
    person_genre_dict = person.genre_dict

    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        for data in request.data:
            # MtoM field 관리
            person.like_genres.add(data)
            # Json field 관리
            person_genre_dict[str(data)] += 1
        person.save()
        return Response(status=status.HTTP_201_CREATED)

# 장르 데이터를 기반으로 영화 추천
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend(request):
    person = get_object_or_404(get_user_model(), username=request.user)
    person_genre_dict = person.genre_dict

    max_val = 0
    best_genre = ''
    for key, val in person_genre_dict.items():
        if val >= max_val:
            max_val = val
            best_genre = key

    if max_val != 0:
        movies = Movie.objects.order_by('?')[:1000]
        recommend_movies = []
        cnt = 0
        for movie in movies:
            if cnt >= 200:
                break
            if int(best_genre) in [x.id for x in movie.genre_ids.all()]:
                recommend_movies.append(movie)
                cnt += 1
                continue

        best_genre = get_object_or_404(Genre, pk=int(best_genre))

        serializer = MovieSerializer(recommend_movies[:50], many=True)
        return JsonResponse({'data': serializer.data, 'best_genre': best_genre.name }, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'best_genre': '아직 데이터가 없는 상태' }, status=status.HTTP_200_OK)



