from django.contrib import admin
from django.urls import path

from purbeurre.views import dashboard, connexion

urlpatterns = [
    path("", dashboard, name='home'),
    path('admin/', admin.site.urls),
    path('connexion/', connexion, name='connexion'),
]
