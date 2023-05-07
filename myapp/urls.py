from django.urls import path
from . import views




urlpatterns = [
    path('', views.index),# '' --- principal rute
    path("about/",views.about),
    path('hello/<int:username>', views.hello),
    path("project/", views.project),
    path("tasks/<int:id>", views.tasks),
]
