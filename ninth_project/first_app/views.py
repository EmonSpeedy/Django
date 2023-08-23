from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name', 'eshmam')
    # response.set_cookie('name', 'jarin', max_age=10)
    response.set_cookie('name', 'jarin', expires=datetime.utcnow()+timedelta(days=3))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'cookie.html', {'name' : name})

def delete_cookie(request):
    response = render(request, 'delete.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    data = {
        'name' : 'eshmam',
        'age' : 11,
        'language' : 'bangla'
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request, 'home.html')

def get_session(request):
    # data = request.session
    # return render(request, 'get_session.html',{'data' : data})
    if 'name' in request.session:
        data = request.session
        name = data.get('name', 'Guest')
        request.session.modified = True
        return render(request, 'get_session.html', {'name' : name})
    else:
        return HttpResponse('Your session has been expired. Set again.')

    # age = data.get('age')
    # language = data.get('language')

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request, 'delete.html')







