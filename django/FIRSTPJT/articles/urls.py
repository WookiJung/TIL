from django.urls import path
from . import views  # 상대적 경로를 명시적으로 표현

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greetings/', views.greetings, name='greetings'),
    path('dinner/', views.dinner, name='dinner'),
    path('throw/', views.throw,name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/',views.hello, name='hello'),
]