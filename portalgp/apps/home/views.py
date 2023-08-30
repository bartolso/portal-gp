from django.shortcuts import render, redirect
from django.contrib import messages
from apps.game.gps.models import GP
from apps.game.mbds.models import MBD
from apps.game.drgs.models import DRG

def home(request):
    gp_count = GP.objects.count()
    mbd_count = MBD.objects.count()
    drg_count = DRG.objects.count()

    return(render(request, 'home/home.html', {'gp_count': gp_count, 'mbd_count': mbd_count, 'drg_count': drg_count}))

def home_start(request):
    return render(request, 'home/home_start.html', {})

def resistencia(request):
    return render(request, 'home/resistencia.html', {})

def about(request):
    return render(request, 'home/about.html', {})