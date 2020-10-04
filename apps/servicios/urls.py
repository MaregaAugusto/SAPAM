
from django.contrib import admin
from django.urls import path
#motodos de render estandar como login
from django.contrib.auth import views as auth

#este es mi archivo
from . import views

#este nombre sirve para llamar a las url en todo el proyecto, exepto en urls de programa principal
app_name="servicios"

urlpatterns = [
    path('listar/', views.Lista_Servicios_Ancianos.as_view(template_name="servicios/listar.htm"), name="listar"),
    path('listar_ca/', views.Lista_Servicios_Colaboradores_activo.as_view(template_name="servicios/listar_ca.htm"), name="listar_ca"),
    path('listar_cf/', views.Lista_Servicios_Colaboradores_finalizados.as_view(template_name="servicios/listar_cf.htm"), name="listar_cf"),
    path('principal_ancianos/', views.crearServicio, name="principal_ancianos"),
    path('finalizar_ser/<int:pk>', views.ServicioFinalizarView.as_view(), name="finalizar_ser"),
    path('denuncia/<int:id>', views.CrearDenuncia, name="denuncia"),
    path('listardenuncias/', views.Lista_Denuncias.as_view(template_name="servicios/listardenuncias.htm"), name="listardenuncias"),
    path('listarmidenuncias/', views.Lista_MiDenuncias.as_view(template_name="servicios/listarmidenuncias.htm"), name="listarmidenuncias"),
    
]


