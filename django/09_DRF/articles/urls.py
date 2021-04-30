from django.urls import path
from . import views
urlpatterns = [
    path('v1/articles/', views.create_or_list_article),
    path('v1/articles/<int:article_pk>/', views.detail_article),
]
