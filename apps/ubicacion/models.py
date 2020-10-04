from django.db import models

# Create your models here.
#idrebap	barrio_nombre	provincia_id	provincia_nombre	departamento_nombre	localidad_nombre

class Provincias(models.Model):
    nombre: models.CharField(max_length=200)

class Ciudad(models.Model):
    nombre: models.CharField(max_length=200)
    provincia: models.OneToOneField(Provincias, verbose_name=("provincia"), on_delete=models.CASCADE)