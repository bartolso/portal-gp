from django.urls import path
from . import views

urlpatterns = [
    path('elections/', views.elections, name='elections'),
    path('elections/29oct', views.oct29, name='29oct'),
]