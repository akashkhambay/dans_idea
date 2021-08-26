from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# videogames = [
#     { 'id': 1, 'title': 'Persona 5', 'stock': True },
#     { 'id': 2, 'title': 'Mario Kart', 'stock': False},
#     { 'id': 3, 'title': 'Wii Sports', 'stock': True}
# ]


# Create your views here.
def index(request):
    games = Game.objects.all()
    context = {"games": games}
    return render(request, 'videogames/game-store.html', context)

def about(request):
    return render(request, 'videogames/about.html')    