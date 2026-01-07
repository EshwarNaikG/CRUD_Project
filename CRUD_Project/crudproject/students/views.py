from django.shortcuts import render, redirect
from .models import Student

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course']
        )
        return redirect('view_students')
    return render(request, 'add.html')

def view_students(request):
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})

def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('view_students')
    return render(request, 'update.html', {'student': student})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('view_students')
