# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# fbv vs cbv

def display(request):
    s = "<h1>Hello, Students! Welcome to Django Class!</h1>"
    return HttpResponse(s)


def greeting(request):
    return HttpResponse("<p>Hello Students!</p>")