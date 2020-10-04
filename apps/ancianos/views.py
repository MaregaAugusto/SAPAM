from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
#controles de login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import RegistroAncianoFrom, ModificarAncianoForm
from .models import Anciano
from apps.usuarios.models import Usuario
from apps.utils import services

import json

# Create your views here.
@login_required
def Principal(request):
	return render(request,'ancianos/principal.htm')

def Nova(request):
	return render(request,'ancianos/nova.htm')

class RegistrarAnciano(CreateView):
	model = Usuario
	form_class = RegistroAncianoFrom
	template_name = 'ancianos/registrar.htm'
	success_url = reverse_lazy('usuarios:login_ancianos')

class RegistrarAnciano2(CreateView):
	model = Usuario
	form_class = RegistroAncianoFrom
	template_name = 'ancianos/r.htm'
	success_url = reverse_lazy('usuarios:login_ancianos')

class AncianoUpdateView(LoginRequiredMixin, UpdateView):
	model = Usuario
	form_class = ModificarAncianoForm
	template_name = "ancianos/modificar.htm"
	success_url = reverse_lazy('servicios:principal_ancianos')
