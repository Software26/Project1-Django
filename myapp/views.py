from django.shortcuts import render
from django.http import HttpResponse, JsonResponse # calling the HttpResponse method
from .models import Project # calling bd

# Create your views here.
def index(request):
    return HttpResponse("Index")

def hello(request,username):
    return HttpResponse("<h1>Hello %s </h1>" % username) # here a param

def about(request):
    return HttpResponse("<h1>About</h1>")

def project(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request):
    return HttpResponse("Tasks")
