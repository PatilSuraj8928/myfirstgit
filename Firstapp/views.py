from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def First(request):
    return HttpResponse ('Hi! This is Suraj!')

def Second(request):
    return HttpResponse('<h1>Hi! This is Suraj</h1>')

def Third(request):
    return HttpResponse ('<h1><marquee>Hi<br> This is Suraj!</marquee></h1>')