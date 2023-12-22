from django.contrib import admin
from django.urls import path, include

from django_rq import urls as rq_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('', include('apps.core.urls')),
    path('', include('apps.home.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.game.gps.urls')),
    path('', include('apps.game.mbds.urls')),
    path('', include('apps.game.drgs.urls')),
    path('', include('apps.wimport.urls')),
    path('', include('apps.dayview.urls')),
    path('', include('apps.tools.urls')),
    path('', include('apps.docs.urls')),
    path('', include('apps.gptests.urls')),
    path('', include('apps.stats.urls')),
    path('', include('apps.scores.urls')),
    path('', include('apps.agenda.urls')),
    path('', include('apps.elections.urls')),
    path('', include('apps.misc.enigdic.urls')),
    path('rq/', include(rq_urls)),
]
