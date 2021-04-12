
# Create your views here.
from django.shortcuts import render, HttpResponse
from blog.models import Blog

def home(request):
    #return HttpResponse("this is home")
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'bloghome.html', context)

def blogpost(request, slug):
    return HttpResponse("you are viewing {slug}")  

def contact(request):
    #return HttpResponse("this is contact")
    return render(request, 'contact.html')

