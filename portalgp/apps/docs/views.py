from django.shortcuts import render, redirect
from django.contrib import messages

def docs(request):
    return render(request, 'docs/docs.html', {})

def docs_db_gp(request):
    return render(request, 'docs/db/gp.html', {})

def docs_db_mbd(request):
    return render(request, 'docs/db/mbd.html', {})

def docs_db_drg(request):
    return render(request, 'docs/db/drg.html', {})

def docs_general_general(request):
    return render(request, 'docs/general/general.html', {})

def docs_que_es_portal_gp(request):
    return render(request, 'docs/docs_que_es_portal_gp.html', {})

def docs_general_datos_walkthrough(request):
    return render(request, 'docs/general/datos_walkthrough.html', {})

def docs_general_info_importante(request):
    return render(request, 'docs/general/info_importante.html', {})

def docs_wimport(request):
    return render(request, 'docs/docs_wimport', {})

def docs_linkear_ids(request):
    return render(request, 'docs/docs_linkear_ids', {})

def docs_usuarios(request):
    return render(request, 'docs/docs_usuarios', {})