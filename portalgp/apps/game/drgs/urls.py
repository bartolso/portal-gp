from django.urls import path
from . import views

urlpatterns = [
    path('drgs/', views.drgs, name='drgs'),
    path('drgs/drg/<int:pk>', views.drg, name='drg'),
    path('drgs/add_drg', views.add_drg, name='add_drg'),
    path('drgs/delete_drg/<int:pk>', views.delete_drg, name='delete_drg'),
    path('drgs/update_drg/<int:pk>', views.update_drg, name='update_drg'),

    path('drgs/get_paginated_data', views.get_paginated_data, name='get_drgs_paginated_data'),
]