from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ScoresCalculatorForm

from apps.persons.models import Person
from apps.game.gps.models import GP

def scores(request):
    return render(request, 'scores/scores.html', {})

def scores_config(request):
    return render(request, 'scores/scores_config.html', {})

def scores_calculator(request):
    form = ScoresCalculatorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Cálculo de resultados
            results = [] # lista de listas de jugador y puntuación
            players = Person.objects.all()
            for player in players:
                player_result = [] # ["nombre", "resultado"]
                player_gps = GP.objects.filter(date__range=(start_date, end_date), person=player, valid="Si")
                score_count = 0

                for gp in player_gps:
                    try:
                        score_count += int(gp.gpv) # el gpv está guardado como string en la base de datos...
                    except Exception:
                        pass
                player_result = [player.name, score_count]
                results.append(player_result)

            results = sorted(results, key=lambda x: x[1], reverse=True)
            print(results)
            return render(request, 'scores/scores_calculator_results.html', {'results':results})
    return render(request, 'scores/scores_calculator.html', {'form':form})

def scores_simulator(request):
    pass