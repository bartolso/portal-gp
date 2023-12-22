from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_start', views.home_start, name='home_start'),
    path('resistencia', views.resistencia, name='resistencia'),
    path('about', views.about, name='about'),
]
