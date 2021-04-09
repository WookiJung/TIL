from django.urls import path
from . import views

app_name ='articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_pk>/detail/', views.detail, name='detail'),
    path('<int:article_pk>/like/', views.like, name='like'),
    path('<int:article_pk>/cancel_like/', views.cancel_like, name='cancel_like'),
]
