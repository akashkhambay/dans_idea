from django.shortcuts import render
from django.http import HttpResponse

videogames = [
    { 'id': 1, 'title': 'Persona 5', 'stock': True },
    { 'id': 2, 'title': 'Mario Kart', 'stock': False},
    { 'id': 3, 'title': 'Wii Sports', 'stock': True}
]


# Create your views here.
def index(request):
    return HttpResponse("Hello, world... Blockbuster is back. Here are the videogames index")

def about(request):
    return render(request, 'videogames/about.html')    