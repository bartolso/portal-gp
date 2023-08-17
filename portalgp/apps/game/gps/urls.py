from django.urls import path
from . import views

urlpatterns = [
    path('gps/', views.gps, name='gps'),
    path('gps/gp/<int:pk>', views.gp, name='gp'),
    path('gps/add_gp', views.add_gp, name='add_gp'),
    path('gps/delete_gp/<int:pk>', views.delete_gp, name='delete_gp'),
    path('gps/update_gp/<int:pk>', views.update_gp, name='update_gp'),
    path('gps/validate_gp/<int:pk>/', views.validate_gp, name='validate_gp'),
    path('gps/get_paginated_data', views.get_paginated_data, name='get_gps_paginated_data'),
]