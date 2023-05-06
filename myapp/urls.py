from django.urls import path
from . import views



urlpatterns = [
    path('', views.hello),# '' --- principal rute
    path("about/",views.about),
    
]
