from django.db import models

# Create your models here.

#connection in sttings of file mysite
class Project(models.Model):
    nama = models.CharField(max_length=200)
    
class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    