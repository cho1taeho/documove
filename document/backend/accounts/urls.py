from django.urls import path
from . import views

urlpatterns = [
    path('api/points/increase/', views.increase_points_api, name='increase_points_api'),
    path('api/points/reduce/', views.reduce_points_api, name='reduce_points_api'),
    path('api/badge/upload/', views.upload_badge_api, name = 'upload_badge_api'),
]
