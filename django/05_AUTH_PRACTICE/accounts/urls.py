from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =[
    path('', views.main, name='main'),
    path('profile/<username>/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/<username>/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.password, name='password'),
]