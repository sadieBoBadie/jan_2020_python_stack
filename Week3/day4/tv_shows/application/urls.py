from django.urls import path
from . import views

urlpatterns = [
    # render GET routes Login
    path('', views.index),

    # render routes Shows
    path('shows', views.dashboard),
    path('shows/new', views.new_page),
    path('shows/<int:show_id>/edit', views.edit_page),
    path('shows/<int:show_id>', views.show_page),

    # redirect routes - actions routes (change the database)
    #login routes
    path('register', views.register),
    path('login', views.login),
    #TV shows
    path('shows/<int:show_id>/delete', views.delete),
    path('shows/create', views.create_show),
    path('shows/<int: show_id>/update', views.update) # make this
]