from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = "__all__"
        labels = {
            'name' : 'Student name',
            'roll' : 'Student Roll'
        }
        help_texts = {
            'name' : 'Type student name here'
        }
        error_messeges = {
            'name' : {'required' : 'Your name is required'}
        }
    