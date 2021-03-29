from django.urls import path

from django.contrib.auth import views
from .forms import LoginForm
from accounts.views import utilisateurs_views, registrer_views


urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True, authentication_form=LoginForm), name="login"),
    path('logout/', views.LogoutView.as_view(template_name='accounts/logout.html', next_page='/accounts/login/'), name="logout"),
    path('utilisateurs/', utilisateurs_views, name='mon_compte'),
    path('register/', registrer_views , name='register'),
    ]
