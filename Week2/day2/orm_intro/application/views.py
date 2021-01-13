from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.

def index(request):
    return HttpResponse("testing testing")

def createUser(request):
    # Use the request.POST to create a new record
    # return redirect to a function renders success.
    all_users = User.objects.all()
