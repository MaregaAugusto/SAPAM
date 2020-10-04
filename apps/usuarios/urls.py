
from django.contrib import admin
from django.urls import path, include
#motodos de render estandar como login
from django.contrib.auth import views as auth

#este es mi archivo
from . import views

#este nombre sirve para llamar a las url en todo el proyecto, exepto en urls de programa principal
app_name="usuarios"

urlpatterns = [
    path('recuperar/', views.Recuperar, name = "recuperar"),
    path('redirecciona/', views.Redirecciona, name = "redirecciona"),

    path('login_ancianos/',auth.LoginView.as_view(template_name="usuarios/login_ancianos.htm"),name="login_ancianos"),
    path('login_colaboradores/',auth.LoginView.as_view(template_name="usuarios/login_colaboradores.htm"),name="login_colaboradores"),
    path('logout/',auth.LogoutView.as_view(),name="logout"),
    path('eliminar/<int:pk>', views.UsuarioDeleteView.as_view(), name="eliminar"),
    
    
    
]