"""SAPAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url de la principal
    path('admin', admin.site.urls),
    path('', views.Index, name='inicio'),


    path('usuarios/',include('apps.usuarios.urls')),
    path('ancianos/',include('apps.ancianos.urls')),
    path('servicios/',include('apps.servicios.urls')),
    path('colaboradores/',include('apps.colaboradores.urls')),
    path('reset_password/',auth.PasswordResetView.as_view(template_name='usuarios/password_reset_form.htm'),name="reset_password"),
    path('reset_password_sent/',auth.PasswordResetDoneView.as_view(template_name='usuarios/password_reset_done.htm'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth.PasswordResetConfirmView.as_view(template_name='usuarios/password_reset_confirm.htm'),name="password_reset_confirm"),
    path('reset_password_complete/',auth.PasswordResetCompleteView.as_view(template_name='usuarios/password_reset_complete.htm'),name="password_reset_complete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
