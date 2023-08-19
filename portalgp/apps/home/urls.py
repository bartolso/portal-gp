from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.home_start, name='home_start'),
    path('resistencia', views.resistencia, name='resistencia'),
]
