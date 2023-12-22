from django.http import JsonResponse
from django.shortcuts import render, redirect
import random

from .models import Cards, CardEntry

def get_cards(request):
    #devuelve un JsonResponse con las cartas y los jugadores.
    data = {}
    cards = Cards.objects.all()
    for card in cards:
        data[f'{card.id}'] = card.card
    
    # los ids se randomizan
    values = list(data.values())
    random.shuffle(values)
    data = {k: values[i] for i, k in enumerate(data.keys())}
    
    return JsonResponse(data)

def enigdic(request):
    return render(request, 'misc/enigdic/enigdic.html', {})