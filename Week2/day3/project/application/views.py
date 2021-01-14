from django.shortcuts import render, redirect
from .models import User

# Create your views here.

# Render functions
def index(request):
    print("in index function")

    context = {
        "all_users": User.objects.all()
    }
    
    # show all users
    return render(request, "index.html", context)

# Note: Since the demo, I broke it into 2 functions unlike the demo 
# so you can see how you might render all 
# of a particular user's cars
def show_cars(request):
    print("in show car function")
    this_user = User.objects.get(id=3)

    context = {
        "this_users_cars": this_user.cars.all()
    }
    return render(request, "show_user_cars.html", context)

# Action 
def create(request):
    print(request.POST["first_name"])
    print("In create function")
    
    # create a new user, with information from a form
    User.objects.create(
        first_name=request.POST["first_name"], 
        last_name=request.POST["last_name"],
        email=request.POST["email"]
        )

    return redirect('/')

def createCar(request):

    this_user = User.objects.get(id = 3)

    Car.objects.create(
        make = "Toyota",
        model = "Corola",
        year = 1998,
        current_owner = this_user
    )
    print("In create function")
    
    # create a new user, with information from a form


    return redirect('/')
