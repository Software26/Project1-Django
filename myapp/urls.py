from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),# '' --- principal rute
    path("about/",views.about),
    path('hello/<int:id>', views.hello)
]
