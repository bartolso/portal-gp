from django.urls import path
from . import views

urlpatterns = [
    path('dayview/', views.day_view, name='day_view'),
    path('dayview/get_day_data', views.get_day_data, name='get_day_data'), #solamente la fecha, nada más
    path('dayview/get_day_info', views.get_day_info, name='get_day_info'),
    path('dayview/get_day_gps_datatable', views.get_day_gps_datatable, name='get_day_gps_datatable'),
    path('dayview/get_validator_data', views.get_validator_data, name='get_validator_data'),
    path('dayview/ajax_validate_gp', views.ajax_validate_gp, name='ajax_validate_gp'),
    #path('dayview/ajax_devalidate_gp', views.ajax_devalidate_gp, name='ajax_devalidate_gp'),
]