from django.urls import path
from . import views

urlpatterns = [
    path('agenda_component/', views.agenda_component, name='agenda_component'),
    path('agenda/', views.agenda, name='agenda'),
    path('agenda/events_json/', views.events_json, name='events_json'),
]