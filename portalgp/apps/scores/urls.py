from django.urls import path
from . import views

urlpatterns = [
    path('scores', views.scores, name='scores'),
    path('scores_config', views.scores_config, name='scores_config'),
    path('scores_calculator', views.scores_calculator, name='scores_calculator'),
]
