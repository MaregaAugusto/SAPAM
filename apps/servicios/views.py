from django.db.models import Min
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.contrib import messages

#importar apps
from apps.usuarios.models import Usuario
from apps.ancianos.models import Anciano
from apps.colaboradores.models import Colaborador
from .models import Servicio, Denuncia
from .forms import FinalizarServicioForm
from datetime import datetime
from django.contrib import messages


# Create your views here.
# vistas denuncia
def CrearDenuncia(request, id):
	ser = Servicio.objects.get(id = id)
	dec = Denuncia.objects.filter(servicio = ser)
	if dec:
		messages.info(request, 'Usted ya realizo un reclamo de este servicio')
	else:
		if request.method == 'POST':
			asunto = request.POST.get('asunto')
			texto = request.POST.get('texto')
			den = Denuncia.objects.create(asunto = asunto, texto = texto, servicio = ser)
			den.save()
			messages.info(request, 'Su reclamo se ha registrado correctamente')
	return render(request,'servicios/denuncia.htm')

class Lista_Denuncias(ListView):
	model=Denuncia
	template_name ='servicios/listardenuncias.htm'
	
	def get_queryset(self):
		datos = super().get_queryset()
		anciano = Anciano.objects.get(usuario_id = self.request.user.id)
		servicio = Servicio.objects.filter(anciano_id = anciano.id)
		aux = list()
		resultado = list()
		x = 0
		for p in servicio:
			aux.append(datos.filter(servicio_id = p.id)[:1])
			if aux[x]:
				resultado.append(aux[x].get())
			x += 1
		return resultado

class Lista_MiDenuncias(ListView):
	model=Denuncia
	template_name ='servicios/listarmidenuncias.htm'
	
	def get_queryset(self):
		datos = super().get_queryset()
		colaborador = Colaborador.objects.get(usuario_id = self.request.user.id)
		servicio = Servicio.objects.filter(colaborador = colaborador.id)
		aux = list()
		resultado = list()
		x = 0
		for p in servicio:
			aux.append(datos.filter(servicio_id = p.id)[:1])
			if aux[x]:
				resultado.append(aux[x].get())
			x += 1
		return resultado



#vista servicios
class Lista_Servicios_Ancianos(ListView):
	model=Servicio
	template_name ='servicios/listar.htm'
	
	def get_queryset(self):
		datos = super().get_queryset()
		anciano = Anciano.objects.get(usuario_id = self.request.user.id)
		datos = datos.filter(anciano = anciano.id)
		return datos

class Lista_Servicios_Colaboradores_activo(ListView):
	model=Servicio
	template_name ='servicios/listar_ca.htm'
	queryset = Servicio.objects.filter(estado = 0)

	def get_queryset(self):
		datos = super().get_queryset()
		colaborador = Colaborador.objects.get(usuario_id = self.request.user.id)
		datos = datos.filter(colaborador = colaborador.id)
		return datos

class Lista_Servicios_Colaboradores_finalizados(ListView):
	model=Servicio
	template_name ='servicios/listar_cf.htm'
	queryset = Servicio.objects.filter(estado = 1)

	def get_queryset(self):
		datos = super().get_queryset()
		colaborador = Colaborador.objects.get(usuario_id = self.request.user.id)
		datos = datos.filter(colaborador = colaborador.id)
		return datos

class ServicioFinalizarView(UpdateView):
	model = Servicio
	form_class = FinalizarServicioForm
	template_name = "servicios/finalizar_ser.htm"
	success_url = reverse_lazy('servicios:listar_ca')


def crearServicio(request):
	if request.method == 'POST':
		tipo = request.POST.get('tipo')
		if tipo == "COMPRA":
			col = Colaborador.objects.filter(compras = 1)
			tareasMin = (col.aggregate(Min('tareas')))['tareas__min']
			col = (col.filter(tareas = tareasMin)[:1]).get()

		elif tipo == "PAGO":
			col = Colaborador.objects.filter(pagos = 1)
			tareasMin = (col.aggregate(Min('tareas')))['tareas__min']
			col = (col.filter(tareas = tareasMin)[:1]).get()

		elif tipo == "TRAMITE":
			col = Colaborador.objects.filter(tramites = 1)
			tareasMin = (col.aggregate(Min('tareas')))['tareas__min']
			col = (col.filter(tareas = tareasMin)[:1]).get()

		anc = Anciano.objects.get(usuario_id= request.user.id)
		Servicio.objects.create(tipo = tipo, anciano = anc, colaborador = col)
		col.tareas = tareasMin + 1
		col.save()
		messages.info(request,'Su solicitud se registró correctamente')

	return render(request,'servicios/principal_ancianos.htm')
