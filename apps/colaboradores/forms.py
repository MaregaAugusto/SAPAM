from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms


#MODELOS
from .models import Colaborador
from apps.usuarios.models import Usuario

class RegistroColaboradorFrom(UserCreationForm):
    compras = forms.BooleanField(required=False, widget = forms.TextInput(attrs = {
                                                    'type':'checkbox',
                                                    'id':'compras',}))
    tramites = forms.BooleanField(required=False, widget = forms.TextInput(attrs = {
                                                    'type':'checkbox',
                                                    'id': 'tramites',}))
    pagos = forms.BooleanField(required=False, widget = forms.TextInput(attrs = {
                                                    'type':'checkbox',
                                                    'id': 'pagos',}))

    class Meta:
        model = Usuario
        fields = ['username','dni','first_name','last_name','email','password1','password2','telefono','provincia','ciudad','barrio','calle','altura','fecha_nacimiento']

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
        user.is_colaborador = True
        user.save()
        Colaborador.objects.create(usuario=user,
                                    compras = self.cleaned_data.get('compras'),
                                    tramites = self.cleaned_data.get('tramites'),
                                    pagos = self.cleaned_data.get('pagos'),)
        return user

class ModificarColaboradorForm(forms.ModelForm):

    compras = forms.BooleanField(required=False, widget = forms.TextInput(attrs = {
                                                    'type':'checkbox',
                                                    'id': 'compras',}))
    tramites = forms.BooleanField(required=False, widget = forms.TextInput(attrs = {
                                                    'type':'checkbox',
                                                    'id': 'tramites',}))
    pagos = forms.BooleanField(required=False, widget = forms.TextInput(attrs = {
                                                    'type':'checkbox',
                                                    'id': 'pagos',}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['compras'].initial = kwargs['instance'].colaborador.compras
        self.fields['tramites'].initial = kwargs['instance'].colaborador.tramites
        self.fields['pagos'].initial = kwargs['instance'].colaborador.pagos


    class Meta:
        model = Usuario
        fields = ['first_name','last_name','telefono','provincia','ciudad','barrio','calle','altura','fecha_nacimiento']

        widgets ={
            'fecha_nacimiento' : forms.TextInput(
                attrs = {
                    'type':'date',
                    'class':'form-control',
                    'id': 'fecha_nacimiento',
                }
            ),
        } 

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.save()
        Colaborador.objects.filter(usuario=user).update(compras = self.cleaned_data.get('compras'),
                                                        tramites = self.cleaned_data.get('tramites'),
                                                        pagos = self.cleaned_data.get('pagos'),)
        return user