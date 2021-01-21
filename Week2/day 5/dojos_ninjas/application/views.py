from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    print("In index route to render page...")
    # Get all the dojos from the db to show in the
    # html page
    
    # set "dojos" key's value to a list of Dojo objects from the db
    context = { 
        "dojos": Dojo.objects.all(),
    }


    return render(request, "index.html", context)

def create_dojo(request):
    print("Creating a dojo...")
    print(request.POST)
    
    # Take form info and create a new dojo
    new_dojo = Dojo.objects.create(
        name=request.POST['name'], 
        city=request.POST['name'], 
        state= request.POST['state']
    )

    print(new_dojo)

    # Go to root route to render the page again
    return redirect('/')

def create_ninja(request):
    print("Creating a ninja...")
    print(request.POST)

    selected_dojo = Dojo.objects.get(id=request.POST["dojo_id"])

    # Take form info and create a new ninja
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo = selected_dojo
    )
    # Go to root route to render the page again
    return redirect('/')