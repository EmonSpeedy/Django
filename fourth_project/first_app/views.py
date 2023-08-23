from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, './first_app/home.html', {"name":"Sahadat", "marks":94,
                                                      "courses": [
                                                          {"id" : 1,
                                                          "course":"C",
                                                          "teacher":"Rahim"},
                                                          {"id" : 2,
                                                           "course":"C++",
                                                          "teacher":"Karim"},
                                                          {"id" : 3,
                                                          "course":"Django",
                                                          "teacher":"Naim"
                                                          }
                                                      ]})

def about(request):
    return render(request, './first_app/about.html', {'author': 'glenn maxwell'})
