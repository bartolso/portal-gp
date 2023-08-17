from django.shortcuts import render

def scores(request):
    return render(request, 'scores/scores.html', {})

def scores_config(request):
    pass