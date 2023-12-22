from django.shortcuts import render

from django.urls import path
from . import views

urlpatterns = [
    path('tools/', views.tools, name='tools'),
    path('tools/link_fk', views.link_fk, name='link_fk'),
    path('tools/calculate_gp_positions', views.calculate_gp_positions_render, name='calculate_gp_positions_render'),
    path('tools/calculate_gp_positions/<str:arg1>', views.calculate_gp_positions, name='calculate_gp_positions'),
    path('tools/calculate_gp_streaks', views.calculate_gp_streaks, name='calculate_gp_streaks'),
    path('tools/calculate_gp_gpvs', views.calculate_gp_gpvs_render, name='calculate_gp_gpvs_render'),
    path('tools/gpv_calculator', views.gpv_calculator, name='gpv_calculator'),
]