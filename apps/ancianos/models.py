from django.db import models
# Create your models here.
# este import es para crear usuarios tiene campos ya estar de django
from apps.usuarios.models import Usuario

class Anciano(models.Model):
	usuario = models.OneToOneField(Usuario, related_name = 'anciano', on_delete=models.CASCADE)
	descripcion = models.TextField(null = True, blank=True)
	telefono = models.BooleanField(default=False) #Teoricamente esto tendria que ser activado por un operador para comprobar que el telefono fue bien ingresado

	def __str__(self):
		return str(self.usuario)
