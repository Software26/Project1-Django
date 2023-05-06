from django.shortcuts import render
from django.http import HttpResponse # calling the HttpResponse method


# Create your views here.
def index(request):
    return HttpResponse("Index")

def hello(request,username):
    return HttpResponse("<h1>Hello %s</h1>" % username) # here a param

def about(request):
    return HttpResponse("<h1>About</h1>")
