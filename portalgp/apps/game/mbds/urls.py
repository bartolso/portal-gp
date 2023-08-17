from django.urls import path
from . import views

urlpatterns = [
    path('mbds/', views.mbds, name='mbds'),
    path('mbds/mbd/<int:pk>', views.mbd, name='mbd'),
    path('mbds/add_mbd', views.add_mbd, name='add_mbd'),
    path('mbds/delete_mbd/<int:pk>', views.delete_mbd, name='delete_mbd'),
    path('mbds/update_mbd/<int:pk>', views.update_mbd, name='update_mbd'),

    path('mbds/get_paginated_data', views.get_paginated_data, name='get_mbds_paginated_data'),
]