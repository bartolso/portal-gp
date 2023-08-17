from django.shortcuts import render
import json
from apps.game.gps.models import GP
from apps.game.mbds.models import MBD
from apps.game.drgs.models import DRG
from apps.persons.models import Person

def stats(request):
    return render(request, 'stats/stats.html', {'gps_by_player_chart': get_chart_gps_by_player(), 
                                                'mbds_by_profeta_chart': get_chart_mbds_by_profeta(),
                                                'drgs_by_profeta_chart': get_chart_drgs_by_profeta(),
                                                })

def get_chart_gps_by_player():
    labels = []
    data = []
    for person in Person.objects.all():
        person_name = person.name
        gp_count = GP.objects.filter(person__name=person_name).count()
        labels.append(person_name)
        data.append(gp_count)

    context = {
        'labels': labels,
        'data': data,
    }

    return json.dumps(context)

def get_chart_mbds_by_profeta():
    labels = []
    data = []
    for person in Person.objects.all():
        person_name = person.name
        mbd_count = MBD.objects.filter(person__name=person_name).count()
        if mbd_count == 0:
            pass
        else:
            labels.append(person_name)
            data.append(mbd_count)

    context = {
        'labels': labels,
        'data': data,
    }

    return json.dumps(context)

def get_chart_drgs_by_profeta():
    labels = []
    data = []
    for person in Person.objects.all():
        person_name = person.name
        drg_count = DRG.objects.filter(person__name=person_name).count()
        if drg_count == 0:
            pass
        else:
            labels.append(person_name)
            data.append(drg_count)

    context = {
        'labels': labels,
        'data': data,
    }

    return json.dumps(context)

def create_chart():
    """
        Esto es para que los usuarios creen su propio gráfico.
        Rango de días a seleccionar y elementos que ver
    """