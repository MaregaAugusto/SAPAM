from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
#Te obliga que para entrar a la viste tengas que estar logeado
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import RegistroColaboradorFrom, ModificarColaboradorForm
from .models import Colaborador
from apps.usuarios.models import Usuario


# Create your views here.
@login_required
def Principal(request):
	return render(request,'colaboradores/principal.htm')

class RegistrarColaborador(CreateView):
	model = Usuario
	form_class = RegistroColaboradorFrom
	template_name = 'colaboradores/registrar.htm'
	success_url = reverse_lazy('usuarios:login_colaboradores')

class ColaboradorUpdateView(LoginRequiredMixin, UpdateView):
	model = Usuario
	form_class = ModificarColaboradorForm
	template_name = "colaboradores/modificar.htm"
	success_url = reverse_lazy('servicios:listar_ca')