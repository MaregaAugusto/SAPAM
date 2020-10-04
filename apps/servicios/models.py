from django.db import models
from apps.ancianos.models import Anciano
from apps.colaboradores.models import Colaborador
# Create your models here.

class Servicio(models.Model):
    tipo = models.CharField(max_length=50) #Tramite, Pago, Compras
    fecha = models.DateField(auto_now=True, auto_now_add = False)
    estado = models.BooleanField(default=False) # en actividad = falso, finalizado = true
    descripcion = models.TextField(null=True, blank=True)
    gasto = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    anciano = models.ForeignKey(Anciano, related_name = 'solicitante',null=True,on_delete = models.SET_NULL)
    colaborador = models.ForeignKey(Colaborador, related_name = 'ayudante',null=True,on_delete = models.SET_NULL)

    class Meta:
        ordering = ["-id"]


class Denuncia(models.Model):
    asunto = models.CharField(max_length=200)
    texto = models.TextField()
    estado = models.BooleanField(default= False) # activo = False, Resuelto = True
    servicio = models.ForeignKey(Servicio,related_name = 'miservicio', null=True, on_delete = models.SET_NULL)