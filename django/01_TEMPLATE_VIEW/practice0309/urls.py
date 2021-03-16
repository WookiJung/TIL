from django.urls import path
from . import views
urlpatterns = [
    path('lotto/<int:value>', views.lotto),
    # /practice0309/var_route/뭐든지들어옴
    path('var_route/<string>/', views.var_route),
    # /practice0309/ping/ -> form으로 사용자 입력받기
    path('ping/', views.ping, name='ping'),
    # /practice0309/pong/ -> 처리결과 보여주기
    path('pong/', views.pong, name='pong'),
]
