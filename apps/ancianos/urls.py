
from django.contrib import admin
from django.urls import path
#motodos de render estandar como login
from django.contrib.auth import views as auth

#este es mi archivo
from . import views

#este nombre sirve para llamar a las url en todo el proyecto, exepto en urls de programa principal
app_name="ancianos"

urlpatterns = [
    
    path('principal/', views.Principal, name = "principal"),

    path('registrar/', views.RegistrarAnciano.as_view(), name="registrar"),
    path('modificar/<int:pk>', views.AncianoUpdateView.as_view(), name="modificar"),

    path('r/', views.RegistrarAnciano2.as_view(), name="r"),
    path('nova/', views.Nova, name = "nova"),
    
]

