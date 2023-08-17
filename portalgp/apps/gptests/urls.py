from django.urls import path
from . import views

urlpatterns = [
    path('gptests/gps/', views.gptests_gps, name='gptests_gps'),
    path('gptests', views.gptests, name='gptests'),
]