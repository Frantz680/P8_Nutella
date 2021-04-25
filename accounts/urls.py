from django.urls import path

from django.contrib.auth import views
from .forms import LoginForm
from accounts.views import my_product_views, registrer_views, my_account_views

urlpatterns = [
    path('login/', views.LoginView.as_view(
        template_name='accounts/login.html',
        redirect_authenticated_user=True,
        authentication_form=LoginForm), name="login"),

    path('logout/', views.LogoutView.as_view(
        template_name='accounts/logout.html',
        next_page='/accounts/login/'), name="logout"),

    path('my_account/<str:product_id>/', my_product_views, name='my_product'),
    path('register/', registrer_views, name='register'),
    path('my_account/', my_account_views, name='my_account'),
]
