from django.urls import path
from . import views

urlpatterns = [
    path('docs/', views.docs, name='docs'),
    path('docs/db/gp', views.docs_db_gp, name='docs_db_gp'),
    path('docs/db/mbd', views.docs_db_mbd, name='docs_db_mbd'),
    path('docs/db/drg', views.docs_db_drg, name='docs_db_drg'),
    path('docs/general', views.docs_general_general, name='docs_general_general'),
    path('docs/general/que_es_portal_gp', views.docs_que_es_portal_gp, name='docs_que_es_portal_gp'),
    path('docs/general/guia_para_añadir_datos', views.docs_general_datos_walkthrough, name='docs_general_datos_walkthrough'),
    path('docs/general/info_importante', views.docs_general_info_importante, name='docs_general_info_importante'),
    path('docs/herramientas/wimport', views.docs_wimport, name='docs_wimport'),
    path('docs/herramientas/linkear_ids', views.docs_linkear_ids, name='docs_linkear_ids'),
    path('docs/portalgp/usuarios', views.docs_usuarios, name='docs_usuarios'),
]