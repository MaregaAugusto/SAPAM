from django.contrib import admin

# Register your models here.
from .models import Servicio, Denuncia

# Register your models here.
admin.site.register(Servicio)

admin.site.register(Denuncia)