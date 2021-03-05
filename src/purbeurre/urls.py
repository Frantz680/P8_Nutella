from django.urls import path

from purbeurre.views import utilisateurs_views

urlpatterns = [
    path('', utilisateurs_views, name='mon_compte'),
]
