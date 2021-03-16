from django.urls import path
from . import views

# URLpattern은 RESTful API로 작성하기.
urlpatterns = [
    # practice/'' -> 전체조회
    path('', views.index, name='index'),
    # practice/'id' -> id조회
    path('<int:pk>/', views.detail, name='detail'),
    # practice/new => 새로운 데이터 입력용 HTML(생성준비단계.)
    path('new/', views.new, name='new'),
    # 사용자 입력 데이터 처리
    path('create/', views.create, name='create'),
    # 사용자 입력을 받기
    path('<int:pk>/edit', views.edit, name='edit'),
    # DB에 업뎃하기
    path('<int:pk>/update', views.update, name='update'),
    # DB에서 지우기.
    path('<int:pk>/delete', views.delete, name='delete'),

]
