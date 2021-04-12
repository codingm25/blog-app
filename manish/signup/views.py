from django.shortcuts import render
from django.http import HttpResponse
from . models import User

# Create your views here.
def signuplogin(request):
    return render(request, 'loginsignup.html')

def signup(request):
    return render(request, 'signup.html') 

def login(request):
    return render(request, 'login.html')

def contacts(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['psw']
    u1=User(name=name, email=email, password=password)
    u1.save()