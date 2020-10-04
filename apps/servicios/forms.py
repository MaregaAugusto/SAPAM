from django import forms
from django.db import transaction
from .models import Servicio, Denuncia


class FinalizarServicioForm(forms.ModelForm):

	class Meta:
		model = Servicio
		fields = ['descripcion','gasto']

	@transaction.atomic
	def save(self):
		ser = super().save(commit=False)
		ser.estado = True
		ser.save()
		return ser
