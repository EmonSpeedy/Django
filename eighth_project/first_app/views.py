from django.shortcuts import render, redirect
from . forms import RegisterForm, ChangeUSerData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def home(request):
    return render(request, './home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account created succesfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form' : form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                # Checking if user is an authentication user
                user = authenticate(username = name, password = userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'form' : form})
    
    else:
        return redirect('profile')
    
def profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUSerData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account updated succesfully')
                form.save()
        else:
            form = ChangeUSerData(instance = request.user)
        return render(request, './profile.html', {'form' : form})
    else:
        return redirect('signup')
    
def user_logout(request):
    logout(request)
    return redirect('login')

def passchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # It will update password
            return redirect('profile')
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request, './passchange.html', {'form':form})

def passchange2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # It will update password
            return redirect('profile')
    else:
        form = SetPasswordForm(user = request.user)
    return render(request, './passchange.html', {'form':form})

def changeuserdata(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ChangeUSerData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account created succesfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUSerData()
        return render(request, './profile.html', {'form' : form})
    else:
        return redirect('signup')
