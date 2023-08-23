from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './first_app/index.html', {"name" : "Sahadat Hossain Emon",
                "marks" : 90, "lists" : [24,5,12,8], "blog" : "I want to be software engineer, In sha Allah. Allah will fulfill my dream."})
    
