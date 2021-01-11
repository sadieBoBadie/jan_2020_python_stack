from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# request.session  = {} --> dictionary

def index(request):
    return render(request, "index.html")

def show_kitties(request):
    return render(request, "kitties.html")

def show_one_kitty(request):

    # context = {
    #     "first_name": request.session["first_name"],
    #     "last_name": request.session["last_name"]
    # }

    return render(request, "kitty.html")

def process_kitty(request):

    print("This is session:", request.session)
    request.session["first_name"] = request.POST["first_name"]
    request.session["last_name"] = request.POST["last_name"]
    # request.POST --> dictionary
    # print("Post: ", request.POST)

    # # request.GET --> dictionary

    print("Processing credit card....")
    # context = {
    #     "first_name": request.POST['first_name'],
    #     "last_name": request.POST['last_name'],
    #     "cc_number": request.POST['cc_number'],
    # }

    return redirect('/show_kitty')