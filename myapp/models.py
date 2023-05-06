from django.db import models

# Create your models here.

#connection in sttings of file mysite
class Project(models.Model):
    nama = models.CharField(max_length=200)