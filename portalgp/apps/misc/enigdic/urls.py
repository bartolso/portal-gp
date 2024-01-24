from django.urls import path
from . import views

urlpatterns = [
    path('enigdic/', views.enigdic, name='enigdic'),
    path('enigdic/welcome', views.welcome, name='welcome'),
    path('enigdic/admin_panel', views.admin_panel, name='admin_panel'),
    path('enigdic/enigma', views.enigma, name='enigma'),
    path('restart_game/', views.restart_game, name='restart_game'),
    path('get_cards/', views.get_cards, name='get_cards'),
    path('get_info/', views.get_info, name='get_info'),
    path('card_change/', views.card_change, name='card_change'),
    path('get_user_card/', views.get_user_card, name='get_user_card'),
    path('get_logs/', views.get_logs, name='get_logs'),
    path('get_scoreboard/', views.get_scoreboard, name='get_scoreboard'),
    path('skip_turn/', views.skip_turn, name='skip_turn'),
]