from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import DRG
from .forms import Add_drg

def drg(request, pk):
    drg = DRG.objects.get(id=pk)
    return render(request, 'game/drgs/drg.html', {'drg':drg})

def get_paginated_data(request):
    search_value = request.GET.get('search[value]')
    queryset = DRG.objects.all()
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
            'valid': item.valid
        }
        for item in page_obj
    ]

    draw = int(request.GET.get('draw', 0))
    return JsonResponse({'data': data, 'recordsTotal': queryset.count(), 'recordsFiltered': paginator.count, 'draw': draw})

def add_drg(request):
    form = Add_drg(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_drg = form.save()
                messages.success(request, "Drg añadido")
                return redirect('home')
        return render(request, 'game/drgs/add_drg.html', {'form':form})
    else:
        messages.error(request, "Debes iniciar sesión")
        return redirect("home")
    
def delete_drg(request, pk):
    if request.user.is_authenticated:
        to_delete = DRG.objects.get(id=pk)
        to_delete.delete()
        messages.success(request, "Drg eliminado.")
        return redirect('drgs')
    else:
        messages.error(request, "Debes iniciar sesión para hacer esto.")
        return redirect('drgs')
    
def update_drg(request, pk):
    if request.user.is_authenticated:
        current_drg = DRG.objects.get(id=pk)
        form = Add_drg(request.POST or None, instance=current_drg)
        if form.is_valid():
            form.save()
            messages.success(request, f"Drg (ID: {current_drg.id}) modificado.")
            return redirect( 'drg', pk=current_drg.id )
    
        return render(request, 'game/drgs/update_drg.html', {'form':form, 'drg': current_drg})
    
    else:
        messages.error(request, "Debes iniciar sesión para hacer esto.")
        return redirect('drgs')
    
def drgs(request):
    drgs = DRG.objects.all()
    return render(request, 'game/drgs/drgs.html', {'drgs':drgs})