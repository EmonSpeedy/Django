from django.shortcuts import render
from first_app.forms import StudentForm
from . models import Student, Teacher

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form' : form})

def showdata(request):
    # students list for one teacher 
    # teacher = Teacher.objects.get(name = 'Tarek')
    # students = teacher.student.all()
    # for stud in students:
    #     print(stud.name)
    # teachers list for one student    
    student = Student.objects.get(name = 'Arup')
    teachers = student.teachers.all()
    for teach in teachers:
        print(teach.name)
    return render(request, 'show_data.html')