from django.shortcuts import render
from django.http import JsonResponse

def agenda_component(request):
    return render(request, 'agenda/agenda_component.html', {})

def agenda(request):
    return render(request, 'agenda/agenda.html', {})

def events_json(request):
    # Retrieve events from your database or any other source
    events = [
        {
            'title': 'Elecciones',
            'start': '2023-08-01',
            'end': '2023-08-05',
        },
        {
            'title': 'Event 2',
            'start': '2023-08-10',
            'color': 'gray', 
        },
        # Add more events...
    ]
    return JsonResponse(events, safe=False)