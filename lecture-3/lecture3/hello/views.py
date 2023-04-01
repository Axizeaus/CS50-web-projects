from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')
    
def greetings(request):
    return HttpResponse('Greetings, earthlings')

def greet_user(request, name):
    return render(request, 'hello/greet.html', {
        'name': name.capitalize()
    })