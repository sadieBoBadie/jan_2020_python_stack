from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    context = {
        "genres" : [
            "Cool", 
            "New Orleans", 
            "Hard Bop", 
            "Progressive",
        ],
        "title" : "Jazz Genres"
    }
    
    return render(request, "index.html", context)

def puppies(request):
    print("Puppies are cute")
    return HttpResponse("Puppies are cute!!")

def kitties(request):
    print("KITTIES are cute")
    return HttpResponse("Kitties are cute!!")