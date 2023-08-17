from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import MBD
from .forms import Add_mbd

def mbd(request, pk):
    mbd = MBD.objects.get(id=pk)
    return render(request, 'game/mbds/mbd.html', {'mbd':mbd})

def get_paginated_data(request):
    search_value = request.GET.get('search[value]')
    queryset = MBD.objects.all()
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
            'drg_time': item.drg.time if item.drg else None,
            'drg_id': item.drg.id if item.drg else None,
            'locked': item.locked,
            'valid': item.valid
        }
        for item in page_obj
    ]

    draw = int(request.GET.get('draw', 0))
    return JsonResponse({'data': data, 'recordsTotal': queryset.count(), 'recordsFiltered': paginator.count, 'draw': draw})

def add_mbd(request):
    form = Add_mbd(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_mbd = form.save()
                messages.success(request, "M.B.D. añadido")
                return redirect('home')
        return render(request, 'game/mbds/add_mbd.html', {'form':form})
    else:
        messages.error(request, "Debes iniciar sesión")
        return redirect("home")
    
def delete_mbd(request, pk):
    if request.user.is_authenticated:
        to_delete = MBD.objects.get(id=pk)
        to_delete.delete()
        messages.success(request, "M.B.D. eliminado.")
        return redirect('mbds')
    else:
        messages.error(request, "Debes iniciar sesión para hacer esto.")
        return redirect('mbds')
    
def update_mbd(request, pk):
    if request.user.is_authenticated:
        current_mbd = MBD.objects.get(id=pk)
        form = Add_mbd(request.POST or None, instance=current_mbd)
        if form.is_valid():
            form.save()
            messages.success(request, f"M.B.D. (ID: {current_mbd.id}) modificado.")
            return redirect( 'mbd', pk=current_mbd.id )
    
        return render(request, 'game/mbds/update_mbd.html', {'form':form, 'mbd': current_mbd})
    
    else:
        messages.error(request, "Debes iniciar sesión para hacer esto.")
        return redirect('mbds')
    
def mbds(request):
    mbds = MBD.objects.all()
    return render(request, 'game/mbds/mbds.html', {'mbds':mbds})