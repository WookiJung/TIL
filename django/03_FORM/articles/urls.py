from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('new/', views.new, name='new'),

    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),

    path('<int:article_pk>/edit/', views.edit, name='edit'),

    path('<int:article_pk>/delete/', views.delete, name='delete'),
]
