from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
from .models import GP
from .forms import Add_gp

def gps(request):
    gps = GP.objects.all()
    return render(request, 'game/gps/gps.html', {'gps':gps})

def get_paginated_data(request):
    search_value = request.GET.get('search[value]')
    queryset = GP.objects.all()
    if search_value:
        queryset = queryset.filter(
            Q(id__icontains=search_value) |
            Q(person__name__icontains=search_value) |
            Q(date__icontains=search_value) |
            Q(time__icontains=search_value)
        )
    
    paginator = Paginator(queryset, 10)  # Number of items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = [
        {
            'id': item.id,
            'person_name': item.person.name,
            'date': item.date,
            'time': item.time,
            'mbd_time': item.mbd.time if item.mbd else None,
            'mbd_id': item.mbd.id if item.mbd else None,
            'drg_time': item.mbd.drg.time if (item.mbd and item.mbd.drg) else None,
            'drg_id': item.mbd.drg.id if (item.mbd and item.mbd.drg) else None,
            'gpv': item.gpv,
            'position': item.position,
            'streak': item.streak,
            'locked': item.locked,
            'valid': item.valid
        }
        for item in page_obj
    ]

    draw = int(request.GET.get('draw', 0))
    return JsonResponse({'data': data, 'recordsTotal': queryset.count(), 'recordsFiltered': paginator.count, 'draw': draw})

def gp(request, pk):
    gp = GP.objects.get(id=pk)
    return render(request, 'game/gps/gp.html', {'gp':gp})

def add_gp(request):
    form = Add_gp(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_gp = form.save()
                messages.success(request, "G.P. añadido")
                return redirect('home')
        return render(request, 'game/gps/add_gp.html', {'form':form})
    else:
        messages.error(request, "Debes iniciar sesión")
        return redirect("home")
    
def delete_gp(request, pk):
    if request.user.is_authenticated:
        to_delete = GP.objects.get(id=pk)
        to_delete.delete()
        messages.success(request, "G.P. eliminado.")
        return redirect('gps')
    else:
        messages.error(request, "Debes iniciar sesión para hacer esto.")
        return redirect('gps')
    
def update_gp(request, pk):
    if request.user.is_authenticated:
        current_gp = GP.objects.get(id=pk)
        form = Add_gp(request.POST or None, instance=current_gp)
        if form.is_valid():
            form.save()
            messages.success(request, f"G.P. (ID: {current_gp.id}) modificado.")
            return redirect('gp', pk=current_gp.id)
        return render(request, 'game/gps/update_gp.html', {'form':form, 'gp':current_gp})
    else:
        messages.error(request, "Debes iniciar sesión para hacer esto.")
        return redirect('gps')
    
def validate_gp(request, pk):
    if request.user.is_authenticated:
        current_gp = GP.objects.get(id=pk)
        current_gp.valid = "Si"
        current_gp.save()

        messages.success(request, f"G.P. (ID: {pk}) validado.")
        return HttpResponse(status=200)
    else:
        messages.error(request, "Debes iniciar sesión para hacer esto.")
        return redirect('gp', pk=current_gp.id)
    
def devalidate_gp(request, pk):
    if request.user.is_authenticated:
        current_gp = GP.objects.get(id=pk)
        current_gp.valid = "No"
        current_gp.save()

        messages.success(request, f"G.P. (ID: {pk}) validado.")
        return HttpResponse(status=200)
    else:
        messages.error(request, "Debes iniciar sesión para hacer esto.")
        return redirect('gp', pk=current_gp.id)
