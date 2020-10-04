from django.db import models
from apps.usuarios.models import Usuario
# Create your models here.

class Colaborador(models.Model):
    usuario = models.OneToOneField(Usuario, related_name = 'colaborador', on_delete=models.CASCADE)
    compras = models.BooleanField(default = False)
    tramites = models.BooleanField(default = False)
    pagos = models.BooleanField(default = False)
    tareas = models.IntegerField(default = 0)

def __str__(self):
    return str(self.usuario)