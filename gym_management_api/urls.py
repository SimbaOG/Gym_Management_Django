"""gym_management_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .authlogin import views

MAIN_DIR = 'gym_management_api'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(f'{MAIN_DIR}.authlogin.urls')),
    # path('/userdata/', include(f'{MAIN_DIR}.authlogin.urls')),
    url(r'^userdata/validate/$', views.validate_reset_info),  # AJAX
    path('user/', include(f'{MAIN_DIR}.authlogin.urls')),
    path('addowner', include(f'{MAIN_DIR}.authlogin.urls')),
    url(r'^confowner/add/$', views.register_owner),  # AJAX
    url(r'^userauth/login/$', views.auth_login_user),
    # path('dashboard/', include(f'{MAIN_DIR}.authlogin.urls'))
]
