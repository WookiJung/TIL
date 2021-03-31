from django.urls import path
from . import views
import random
from .models import Article

app_name = 'vote'
# ran_num = random.choice(Article.objects.all().values('pk'))
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_pk>/detail/', views.detail, name='detail'),
    path('<int:article_pk>/comments/', views.create_comments, name='create_comments'),
    # path(f'{ran_num}/detail/', views.detail, name='random'),
]
