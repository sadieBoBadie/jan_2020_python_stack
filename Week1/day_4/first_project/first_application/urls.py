from django.urls import path
from . import views

print("In applications urls.py")

urlpatterns = [
    path('', views.index),
    path('pups', views.puppies),
    path('cats', views.kitties)
]