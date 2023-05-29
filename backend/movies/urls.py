from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/', views.movie_detail, name='movie_detail'),
    path('genres/', views.genres, name='genres'),
    path('recommend/', views.recommend, name='recommend'),
    path('giving/', views.giving, name='giving'),
    path('movies/', views.movies, name='movies'),
    path('movies/<int:pk>/', views.movie_detail, name='movie-detail'),
    path('totalPointByTheme', views.totalPointByTheme)
]
