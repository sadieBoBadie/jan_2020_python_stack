from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, "index.html")

def show_kitties(request):
    return render(request, "kitties.html")

def show_one_kitty(request, kitty_id):
    print("Kitty id: ", kitty_id)
    return render(request, "kitty.html", {"k_id": kitty_id})

def process_kitty(request):
    print("Post: ", request.POST)
    print("Get: ", request.GET)
    print("In process kitties")


    context = {
        "first_name": request.POST['first_name'],
        "last_name": request.POST['last_name'],
        "email": request.POST['email'],
    }

    return render(request, "kitty.html", context)