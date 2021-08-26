from django.shortcuts import render
from django.http import HttpResponse
#from .models import tbc

# videogames = [
#     { 'id': 1, 'title': 'Persona 5', 'stock': True },
#     { 'id': 2, 'title': 'Mario Kart', 'stock': False},
#     { 'id': 3, 'title': 'Wii Sports', 'stock': True}
# ]


# Create your views here.
def index(request):
    # get the info for each game.
    # pass that as context
    return render(request, '', context)

def about(request):
    return render(request, 'videogames/about.html')    