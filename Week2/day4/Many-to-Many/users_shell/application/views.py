from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print("in index route")
    # Do I need anything from the DB?
    # Yes, all dojos?? All ninjas?

    return render(request, "index.html")

# from sorm submit on ninja form
def createNinja(request):

    print("In create ninja.")
    print("*************************")
    print(request.POST)
    # take form info and create a ninja.

    return redirect('/')

def createDojo(request):

    print("In create dojo.")
    print(request.POST)
    # take form info and create a dojo.

    return redirect('/')

