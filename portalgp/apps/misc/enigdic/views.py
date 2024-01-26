from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db.models import Sum
import random, json, datetime

from .models import Cards, CardEntry, Log, UserScore, Turn, Prisopunto
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
    save_log(request, timestamp_json=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'), text=log_text, tags=['cardupdate'])

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

def get_scoreboard(request):
    json_scores = {}
    for player_id in range(1, 12):
        score_sum = UserScore.objects.filter(person_id=player_id).aggregate(total_sum=Sum('score'))
        json_scores[player_id] = score_sum

    return JsonResponse(json_scores)

def calculate_scores(team1_points, team2_points):
    #devuelve una lista con las puntuaciones para cada equipo ej. [1, 2] (rojo, verde).
    total_points = team1_points + team2_points
    if team1_points == team2_points:
        score_team1 = score_team2 = 2
    else:
        point_difference = abs(team1_points - team2_points)
        print(point_difference)
        if point_difference == 2:
            winner = min(team1_points, team2_points)
            loser = max(team1_points, team2_points)
            score_team1 = 5 if team1_points == winner else 2
            score_team2 = 5 if team2_points == winner else 2
        elif point_difference == 4:
            winner = min(team1_points, team2_points)
            loser = max(team1_points, team2_points)
            score_team1 = 10 if team1_points == winner else 1
            score_team2 = 10 if team2_points == winner else 1
        elif point_difference == 6:
            winner = min(team1_points, team2_points)
            loser = max(team1_points, team2_points)
            score_team1 = 20 if team1_points == winner else 1
            score_team2 = 20 if team2_points == winner else 1
        elif point_difference == 8:
            winner = min(team1_points, team2_points)
            loser = max(team1_points, team2_points)
            score_team1 = 30 if team1_points == winner else 1
            score_team2 = 30 if team2_points == winner else 1

    return [score_team1, score_team2]

def get_card_count():
    cards = Cards.objects.all()

    count_roja = cards.filter(card='roja').count()
    count_verde = cards.filter(card='verde').count()
    print([count_roja, count_verde])
    return [count_roja, count_verde]

@permission_required('enigdic.add_turn', raise_exception=True)
def skip_turn(request=None):
    if request:
        if request.user.is_authenticated:
            # nuevo turno
            last_turn = Turn.objects.latest('timestamp')
            last_turn_number = last_turn.number

            new_turn = Turn(number=last_turn_number+1)
            new_turn.save()

            cards = Cards.objects.all()

            card_count = get_card_count()
            scores = calculate_scores(card_count[0], card_count[1])
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

def cmd_skip_turn():
    # solamente ejecutado des del comando
    last_turn = Turn.objects.latest('timestamp')
    last_turn_number = last_turn.number

    new_turn = Turn(number=last_turn_number+1)
    new_turn.save()

    cards = Cards.objects.all()

    card_count = get_card_count()
    scores = calculate_scores(card_count[0], card_count[1])
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
    save_log(request=None, text=log_text, tags=['turninfo'], timestamp_json=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

    return JsonResponse({'pasar turno': 'ok'})

@permission_required('enigdic.add_turn', raise_exception=True)
def restart_game(request):
    #nuevo turno
    new_turn = Turn(number=1)
    new_turn.save()
    UserScore.objects.all().delete()
    Log.objects.all().delete()
    #Prisopunto.objects.all().delete()

    log_text = f"El juego ha empezado."
    save_log(request=None, text=log_text, tags=['gameinfo'], timestamp_json=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

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

def save_log(request, timestamp_json, text, tags=[]): #qutiado request
    json = {'timestamp': timestamp_json, 'text':text, 'tags':tags}
    log = Log(json=json)
    log.save()


def enigma(request):
    return render(request, 'misc/enigdic/enigma.html')

def censor_json_log(obj, old_str, new_str):
    if isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = censor_json_log(value, old_str, new_str)
    elif isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = censor_json_log(obj[i], old_str, new_str)
    elif isinstance(obj, str):
        return obj.replace(old_str, new_str)
    return obj


def get_logs(request, is_censored=False):
    logs = Log.objects.all()
    json_data = {}
    for log in logs:
        log_id = log.id
        log_json = log.json
        json_data[log_id] = log_json

    if request.user.is_authenticated and request.user.username == 'aitor':
        return JsonResponse(json_data)
    player_list = ['Joaquin', 'Nerea', 'Laura', 'Aitor', 'Sergio', 'Anton', 'Aina', 'Diego', 'Miranda', 'Paula', 'Pablo']
    for player_name in player_list:
        json_data = censor_json_log(json_data, old_str=player_name, new_str='Alguien')

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