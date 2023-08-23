from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    address = models.TextField()

# abstract model
class CommonInfoModel(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    class Meta:
        abstract = True
        
class StudentInfoModel(CommonInfoModel):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=20)
    
class TeacherInfoModel(CommonInfoModel):
    salary = models.IntegerField()
    
# Multable inheritance

class EmployeeModel(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)
    
class ManagerModel(EmployeeModel):
    takes_interview = models.BooleanField()
    hiring = models.BooleanField()
    
# proxy model 

class Friend(models.Model):
    school = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    attendence = models.BooleanField()
    hw = models.BooleanField()
    
class Myself(Friend):
    class Meta:
        proxy = True
        ordering = ['id']

# One to One relationship
class Person(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    
    def __str__(self):
        return self.name
    
    
class Passport(models.Model):
    user = models.OneToOneField(to = Person, on_delete = models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()
    
# One to Many OR Many to One relationship

class Post(models.Model):
    user = models.ForeignKey(Person, on_delete = models.SET_NULL, null = True)
    caption = models.CharField(max_length=50)
    details = models.CharField(max_length=50)

# Many to Many relationship

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    
class Teacher(models.Model):
    student = models.ManyToManyField(Student, related_name = 'teachers')
    name = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    contact = models.CharField(max_length=11)
    
    def student_list(self):
        return ",".join([str(i) for i in self.student.all()])
    
