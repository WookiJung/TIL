from django.shortcuts import render

# Create your views here.

def new(request):
    return render(request, 'new.html')


def index(request):
    return render(request, 'index.html')
