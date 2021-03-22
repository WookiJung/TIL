from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
# Create your views here.
# retrieve/read
def index(request):
    students = Student.objects.all()
    context = {
        'students' : students,
    }
    return render(request, 'orm_practice/index.html', context)

def detail(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student' : student
    }
    return render(request, 'orm_practice/detail.html', context)
# create
def new(request):
    # DB에 넣을 말들 기록하는 페이지 호출
    return render(request, 'orm_practice/new.html')

def create(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        student.major = request.POST.get('major')
        student.age = request.POST.get('age')
        student.intro = request.POST.get('intro')
        student.save()
    # 진짜 DB에 때려박는 코드
        return redirect('detail', pk=student.id)

    # 기존 데이터 수정 HTML
def edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
    }
    return render(request, 'orm_practice/edit.html', context)
    # 수정된 입력데이터 처리.
def update(request, pk):
    student = Student.objects.get(pk=pk)
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.major = request.POST.get('major')
    student.intro = request.POST.get('intro')
    student.save()
    return redirect('detail', pk=student.pk)
    # 데이터 삭제.
def delete(request, pk):
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return redirect('index')
    return redirect('detail', pk=pk)
