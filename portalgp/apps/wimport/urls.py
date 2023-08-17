from django.urls import path
from . import views

urlpatterns = [
    path('wimport', views.wimport, name='wimport'),
    path('upload_wtext_to_db', views.upload_wtext_to_db, name='upload_wtext_to_db'),
]
