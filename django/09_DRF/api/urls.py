from django.urls import path
from . import views

urlpatterns = [
    path('v1/artists/', views.artist_list),
    path('v1/artists/<int:artist_pk>/', views.artist_detail),
    path('v1/artists/<int:artist_pk>/music/', views.create_music_info),
    path('v1/music/', views.music_list),
    path('v1/music/<int:music_pk>/', views.music_detail),
]
