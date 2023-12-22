from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.http import JsonResponse
import datetime
from datetime import date
from apps.game.gps.models import GP
from apps.game.mbds.models import MBD
from apps.game.drgs.models import DRG

def day_view(request):
    return render(request, 'dayview/dayview.html', {})

def get_day_data(request):
    if request.method == 'GET' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        selected_date = request.GET.get('date')
        print(selected_date)
        offset = int(request.GET.get('offset', 0))

        selected_day = datetime.datetime.strptime(selected_date, '%Y-%m-%d').date() + datetime.timedelta(days=offset)
        
        response_data = {
            'selected_day': selected_day.strftime('%Y-%m-%d')
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request'})
    
def get_day_gps_datatable(request):
    selected_date = request.GET.get('selectedDate')
    selected_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d").date()

    queryset = GP.objects.filter(date=selected_date)
    
    paginator = Paginator(queryset, 150)  # Number of items per page
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
            'valid': item.valid
        }
        for item in page_obj
    ]

    draw = int(request.GET.get('draw', 0))
    return JsonResponse({'data': data, 'recordsTotal': queryset.count(), 'recordsFiltered': paginator.count, 'draw': draw})

def get_day_info(request):
    if request.method == 'GET':
        selected_date = request.GET.get('date')
        selected_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d").date()
        mbd_queryset = MBD.objects.filter(date=selected_date)
        drg_queryset = DRG.objects.filter(date=selected_date)

        data = {
            'mbd_time': mbd_queryset[0].time if mbd_queryset else None,
            'mbd_id': mbd_queryset[0].id if mbd_queryset else None,
            'drg_time': drg_queryset[0].time if drg_queryset else None,
            'drg_id': drg_queryset[0].id if drg_queryset else None,
        }

        return JsonResponse(data)
    else:
        pass

def get_validator_data(request):
    if request.method == 'GET':
        selected_date = request.GET.get('date')
        selected_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d").date()

        players = ['Joaquin', 'Nerea', 'Laura', 'Aitor', 'Sergio', 'Anton', 'Aina', 'Diego', 'Miranda', 'Paula', 'Pablo']
        data = {}

        for name in players:
            try:
                person_data = GP.objects.filter(date=selected_date, person__name=name)[0] #hay que ver que pasa cuando hay más de un gp...
                data[f'{name.lower()}_valid'] = person_data.valid
                data[f'{name.lower()}_id'] = person_data.id
            except Exception:
                pass
        return JsonResponse(data)
    
def ajax_validate_gp(request):
    if request.user.is_authenticated:
        selected_date = request.GET.get('date')
        player_name = request.GET.get('player_name')
        current_gp = GP.objects.filter(person__name=player_name, date=selected_date)[0]
        if current_gp.valid == 'Sin revisar':
            current_gp.valid = "Si"
            current_gp.save()
        else:
            if current_gp.valid == 'Si':
                current_gp.valid = "No"
                current_gp.save()
            else:
                if current_gp.valid == 'No':
                    current_gp.valid = "Si"
                    current_gp.save()

        data = {
            'done': 'done'
        }

        return JsonResponse(data)
    