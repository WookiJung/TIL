from django.shortcuts import render
import random

# Create your views here.
def index(request):  # 첫번째 인자는 반드시 request
    return render(request, 'index.html')  # 1번째 request, 2번째 인자로 '탬플릿 폴더 안의 경로'써줘야됨

def greetings(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'Harry'
    }
    context = {'info': info,
               'foods': foods,
    }  # key,value값의 이름은 맞추는게 일반적이다.
    return render(request, 'greetings.html', context)

def dinner(request):
    foods = ['족발','치킨', '피자','국밥','초밥']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods' : foods
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    # print(message)
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)
