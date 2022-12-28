from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

## Creating a template
def index(request):
    return render(request, "hello/index.html") #HTTP response is a special class created by Django. Need to import it at the top of the codebase

def ashley(request):
    return HttpResponse("Hello Ashley")

def jl(request):
    return HttpResponse("Hello JL")

def greet(request, name):
    return render(request, "hello/greet.html",{"name":name.capitalize()}) #HTTP response is a special class created by Django

