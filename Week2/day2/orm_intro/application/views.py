from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.

def index(request):
    # Get all users from the database to show on the page.
    all_users = User.objects.all()
    return render(request, "index.html", {"all_users": all_users})

def createUser(request):
    # Use the request.POST to create a new record
    # return redirect to a function renders success.
    
    return redirect('/')
