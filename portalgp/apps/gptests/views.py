from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from apps.game.gps.models import GP

def gptests_gps(request):
    gps = GP.objects.all()
    return render(request, 'gptests/gps.html', {'gps':gps})

def gptests(request):
    return render(request, 'gptests/gptests.html', {})

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
            'drg_time': item.mbd.drg.time if item.mbd else None,
            'drg_id': item.mbd.drg.id if item.mbd else None,
            'gpv': item.gpv,
            'position': item.position,
            'streak': item.streak,
            'valid': item.valid
        }
        for item in page_obj
    ]

    draw = int(request.GET.get('draw', 0))
    return JsonResponse({'data': data, 'recordsTotal': queryset.count(), 'recordsFiltered': paginator.count, 'draw': draw})