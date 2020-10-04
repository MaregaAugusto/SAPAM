from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms


#MODELOS
from .models import Anciano
from apps.usuarios.models import Usuario

class RegistroAncianoFrom(UserCreationForm):
    descripcion = forms.CharField (required=False, widget = forms.TextInput(attrs = {
                                                    'id': 'descripcion',}))
    class Meta:
        model = Usuario
        fields = ['username','first_name','last_name','email','dni','password1','password2','telefono','provincia','ciudad','barrio','calle','altura','descripcion','fecha_nacimiento']
        widgets ={
            'fecha_nacimiento' : forms.TextInput(
                attrs = {
                    'type':'date',
                    'id': 'fecha_nacimiento',
                }
            ),
        }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_anciano = True
        user.save()
        Anciano.objects.create(usuario=user,
                                descripcion = self.cleaned_data.get('descripcion'))
        return user

class ModificarAncianoForm(forms.ModelForm):

    descripcion = forms.CharField (required=False, widget = forms.TextInput(attrs = {
                                                    'id': 'descripcion',}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].initial = kwargs['instance'].anciano.descripcion

    class Meta:
        model = Usuario
        fields = ['first_name','last_name','email','telefono','provincia','ciudad','barrio','calle','altura','fecha_nacimiento']
        widgets ={
            'fecha_nacimiento' : forms.TextInput(
                attrs = {
                    'type':'date',
                    'id': 'fecha_nacimiento',
                }
            ),
        }
    

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        Anciano.objects.filter(usuario=user).update(descripcion = self.cleaned_data.get('descripcion'))
        return user