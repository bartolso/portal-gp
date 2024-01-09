from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
import random, json, datetime

from .models import Cards, CardEntry, Log, UserScore, Turn
from .forms import ProfetaMessage

def get_cards(request):
    #devuelve un JsonResponse con las cartas y los jugadores aleatorios.
    data = {}
    cards = Cards.objects.all()
    for card in cards:
        data[f'{card.id}'] = card.card

    del data["4"] #eliminar la carta del profeta (existe carta del profeta para que los ids se correspondan a los de los jugadores)
    
    # los ids se randomizan
    values = list(data.values())
    random.shuffle(values)
    data = {k: values[i] for i, k in enumerate(data.keys())}
    
    return JsonResponse(data)

def card_change(request):
    if request.method == 'GET' and request.user.is_authenticated:
        logged_in_user = request.user

        received_data = request.GET.get('data_sent') #verde, roja
        cards = Cards.objects.all()
        for card in cards:
            if card.person.name.lower() == str(logged_in_user):
                card.card = received_data
                card.save()

                make_card_entry(request, cardtype=received_data, player=card.person)

    response = {
            'done': 'done'
        }
    return JsonResponse(response)

def make_card_entry(request, cardtype, player):
    #introduce un cardentry

    new_entry = CardEntry(card=cardtype, person=player)
    new_entry.save()

    log_text = f"{new_entry.person.name} ha cambiado su carta a {cardtype}"
    save_log(request, timestamp_json=new_entry.created_at.strftime('%d-%m-%Y %H:%M:%S'), text=log_text, tags=['cardupdate'])

def get_user_card(request):
    if request.method == 'GET' and request.user.is_authenticated:
        logged_in_user = request.user
    data = {}
    cards = Cards.objects.all()
    for card in cards:
        data[f'{card.id}'] = card.card
        if card.person.name.lower() == str(logged_in_user):
            card_type = card.card
        
    response = {
        'card': card_type
    }

    return JsonResponse(response)

def get_scores(red_cards, green_cards):
    #devuelve una lista con las puntuaciones para cada equipo ej. [1, 2] (rojo, verde).
    red_cards = 5
    green_cards = 5
    return [5, 5]

@permission_required('enigdic.add_turn', raise_exception=True)
def skip_turn(request):
    if request.user.is_authenticated:
        # nuevo turno
        last_turn = Turn.objects.latest('timestamp')
        last_turn_number = last_turn.number

        new_turn = Turn(number=last_turn_number+1)
        new_turn.save()

        cards = Cards.objects.all()
        scores = get_scores(5,4)
        for card in cards:
            card_type = card.card
            player = card.person
            #crear userscore del presente jugador
            if card_type == 'roja':
                userscore = UserScore(person=player, score=scores[0], turn=new_turn)
            if card_type == 'verde':
                userscore = UserScore(person=player, score=scores[1], turn=new_turn)
            userscore.save()

        log_text = f"Día {str(last_turn_number)} finalizado. Empezando nuevo día."
        save_log(request, text=log_text, tags=['turninfo'], timestamp_json=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

    return JsonResponse({'pasar turno': 'ok'})

@permission_required('enigdic.add_turn', raise_exception=True)
def restart_game(request):
    #nuevo turno
    new_turn = Turn(number=1)
    new_turn.save()
    return JsonResponse({'nuevo turno': new_turn.number})

def admin_panel(request):
    if request.method == 'POST':
        form = ProfetaMessage(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            save_log(request, text=message, tags=['profeta_message'], timestamp_json=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    else:
        form = ProfetaMessage()
    return render(request, 'misc/enigdic/admin_panel.html', {'form': form})

def save_log(request, timestamp_json, text, tags=[]):
    json = {'timestamp': timestamp_json, 'text':text, 'tags':tags}
    log = Log(json=json)
    log.save()

def enigma(request):
    return render(request, 'misc/enigdic/enigma.html')

def get_logs(request, is_censored=False):
    logs = Log.objects.all()
    json_data = {}
    for log in logs:
        log_id = log.id
        log_json = log.json
        json_data[log_id] = log_json

    #updated_json = json.dumps(json_data, indent=2)

    return JsonResponse(json_data)

def get_info(request):
    info = {}

    # turno actual
    current_turn_number = Turn.objects.latest('timestamp').number
    info['turn_number'] = current_turn_number

    return JsonResponse(info)

def enigdic(request):
    return render(request, 'misc/enigdic/enigdic.html', {})

def welcome(request):
    return render(request, 'misc/enigdic/welcome.html', {})