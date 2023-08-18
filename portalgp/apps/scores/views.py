from django.shortcuts import render

def scores(request):
    return render(request, 'scores/scores.html', {})

def scores_config(request):
    return render(request, 'scores/scores_config.html', {})

def scores_simulator(request):
    pass