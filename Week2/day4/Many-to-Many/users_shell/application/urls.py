
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # render routes
    path('', views.index),

    #action routes
    path('createNinja'),
    path('creatDojo')
]
