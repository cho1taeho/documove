from django.urls import path
from . import views


app_name = 'community'

urlpatterns = [
    path('reviews/', views.review_create),
    path('reviews/<int:review_pk>/', views.review_update_delete),
    path('reviews/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_update_delete),
    path('moviepoints/<int:movie_pk>/', views.moviepoint)
]