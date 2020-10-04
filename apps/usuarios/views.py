from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from .models import Usuario

# Create your views here.

def Recuperar(request):
	return render(request,'usuarios/recuperar.htm')

def Redirecciona(request):
	return render(request,'usuarios/redirecciona.htm')

class UsuarioDeleteView(DeleteView):
	model = Usuario
	success_url = reverse_lazy('ancianos:principal')