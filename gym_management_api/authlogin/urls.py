from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('reset-password', views.load_pass_reset, name='load_pass_reset'),
    path('validate', views.validate_reset_info, name='validate_reset_info'),
    path('authrpass', views.auth_reset_pass, name='auth_reset_pass'),
    path('addowner', views.auth_master, name='auth_master'),
    path('dashboard', views.auth_login_user, name='auth_login_user'),
]