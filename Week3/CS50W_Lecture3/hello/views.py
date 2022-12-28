from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello There") #HTTP response is a special class created by Django. Need to import it at the top of the codebase

def ashley(request):
    return HttpResponse("Hello Ashley")

def jl(request):
    return HttpResponse("Hello Jun Long")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")