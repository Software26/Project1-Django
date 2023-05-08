from django.shortcuts import render
from django.http import HttpResponse, JsonResponse # calling the HttpResponse method
from .models import Project, Task # calling bd
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


def hello(request,username):
    return HttpResponse("<h1>Hello %s </h1>" % username) # here a param


def project(request):
   # projects = list(Project.objects.values())
    return render(request,"project.html")

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    return render(request,"task.html")

