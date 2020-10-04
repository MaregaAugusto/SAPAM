from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
# este import es para crear usuarios tiene campos ya estar de django
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser): 
	dni = models.IntegerField(unique=True, null=True)
	provincia = models.CharField(max_length=20, null=True)
	ciudad = models.CharField(max_length=50, null=True)
	barrio = models.CharField(max_length=50, null=True)
	calle = models.CharField(max_length=80, null=True)
	altura = models.IntegerField(null=True)
	fecha_nacimiento = models.DateField(null = True)
	is_anciano = models.BooleanField(default=False)
	is_colaborador = models.BooleanField(default=False)

	""" foto = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None) """
	
	phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="El número de teléfono debe ingresarse en el formato: +999999999. Se permiten hasta 15 dígitos.."
    )
	telefono = models.CharField(validators=[phone_regex], max_length=17)


