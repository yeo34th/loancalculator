from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Web Home</h1>')

def about(request):
    return HttpResponse('<h1>About Home</h1>')

# Create your views here.
