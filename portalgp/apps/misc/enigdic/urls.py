from django.urls import path
from . import views

urlpatterns = [
    path('enigdic/', views.enigdic, name='enigdic'),
    path('get_cards/', views.get_cards, name='get_cards'),
]