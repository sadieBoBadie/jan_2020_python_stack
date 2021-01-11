from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('show_kitties', views.show_kitties),
    path('show_kitty', views.show_one_kitty),
    path('process_kitty', views.process_kitty)
]