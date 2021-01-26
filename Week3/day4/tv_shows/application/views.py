from django.shortcuts import render, redirect
from .models import Show, User
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    print(request.POST)
    print("in reg")
    errors = User.objects.registrationValidator(request.POST)

    if errors:
        for category, message in errors.items():
            messages.error(request, message, extra_tags=category)
        return redirect('/')

    pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        email = request.POST["email"],
        pw_hash = pw_hash
    )

    request.session["user_id"] = new_user.id

    return redirect('/home')

def login(request):
    print(request.POST)
    print("in log")

    return redirect('/')


def dashboard(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "dashboard.html", context)

def new_page(request):
    return render(request, "new.html")

def edit_page(request, show_id):
    # GET THE SHOW FROM THE DB
    context = {
        "show": Show.objects.get(id=show_id)
    }
    print("edit show id: ", show_id)
    return render(request, "edit.html", context)

def show_page(request, show_id):
    # GET THE SHOW FROM THE DB
    print("show page id: ", show_id)

    return render(request, "show.html", context)





# Action and Post routes (will redirect)
def delete(request, show_id):
    print("delete show id: ", show_id)
    # delete something in the db!
    return redirect('/shows')

def create_show(request):
    print("Create show in DB function")
    print(request.POST)

    Show.objects.create(
        title = request.POST['title'],
        description = request.POST['title'],
        network = request.POST['title'],
        release_date = request.POST['title']
    )

    return redirect('/shows/1')

def update(request, show_id):
    print("Update show in DB function")
    print(request.POST)

    errors = Show.objects.basic_validator(request.POST)

    if errors:
        for key in errors:
            messages.error(request, errors[key])
        return redirect(f'/shows/{show_id}/edit')
    
    # errors in session?
    # if any are blank -- errors -- redirect to /shows/1/edit

    show_to_update = Show.objects.get(id=show_id)
    show_to_update.title = request.POST["title"]
    show_to_update.release_date = request.POST["release_date"]
    show_to_update.description = request.POST["description"]
    show_to_update.network = request.POST["network"]

    return redirect(f'/shows/{show_id}')

