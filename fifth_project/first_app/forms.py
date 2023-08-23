from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="Full Name:", initial="Rahim", help_text='Enter your full name here', required=False, widget= forms.Textarea(attrs={'id':'text_area', 'class': 'class1 class2', 'placeholder': 'Enter your name'}))
    file = forms.FileField()
    email = forms.EmailField(label="Email address")
    # age = forms.IntegerField(label="Age")
    # weight = forms.FloatField(label="Weight")
    # balance = forms.DecimalField(label="Balance")
    age = forms.CharField(widget=forms.NumberInput)
    date = forms.CharField(label="Birthdate", widget=forms.DateInput(attrs={'type':'date'}))
    check = forms.BooleanField(label="check")
    appoinment = forms.CharField(label="Appoinment", widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICE = [('S', 'small'), ('M', 'medium'), ('L', 'large')]
    size = forms.ChoiceField(choices= CHOICE, widget=forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices= MEAL, widget=forms.CheckboxSelectMultiple)
    
    
# class StudentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 11:
#             raise forms.ValidationError("Enter at least 10 characters")

#         if '.com' not in valemail:
#             raise forms.ValidationError("Email should contain .com")
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 11:
    #         raise forms.ValidationError("Enter at least 10 characters")
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Email should contain .com")
    #     return valemail

# py manage.py runserver
def check_of_len(value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 characters")
class StudentForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message='Enter a name at least 10 characters')])
    text = forms.CharField(widget=forms.TextInput, validators=[check_of_len])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email address')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(20, message='age must be maximum 20 chars'), validators.MinValueValidator(15, message='age must be minimum 15 chars')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg'], message='Extension must be .pdf or .jpg')])
    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        valname = self.cleaned_data['username']
        if val_pass != val_conpass:
            raise forms.ValidationError("Password didn't match")
        if len(valname) < 8:
            raise forms.ValidationError("Username must be length of 8 characters")
    
    