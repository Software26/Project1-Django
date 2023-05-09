from django.shortcuts import render
from django.http import HttpResponse, JsonResponse # calling the HttpResponse method
from .models import Project, Task # calling bd
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    title = "Django Hola"
    return render(request,"index.html",{"title":title})

def about(request):
    username = " ****it n/'s a hello for about***"
    return render(request,"about.html",{"username" : username})


def hello(request,username):
    return HttpResponse("<h1>Hello %s </h1>" % username) # here a param


def project(request):
   # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,"project.html", {
        "projects" : projects
    })

def tasks(request):
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request,"task.html",{
        "tasks": tasks
    })

