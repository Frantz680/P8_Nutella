from django.urls import path, include

from purbeurre.views import home


urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
]
