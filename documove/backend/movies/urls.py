from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    # path('random/', views.random),
    path('genres/', views.genres, name='genres'),
    path('recommend/', views.recommend, name='recommend'),
    path('giving/', views.giving, name='giving'),
]
