from django.urls import path, include

from purbeurre.views import home, search


urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('search/', search, name='search'),
]
