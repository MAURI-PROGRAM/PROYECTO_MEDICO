from django import forms
from .models import Paciente
from django.utils.timezone import now
from django.utils import timezone

class PacienteForm(forms.Form):
    cedula_id = forms.CharField(label='CEDULA', max_length=100)
    nombre_uno = forms.CharField(label='PRIMER NOMBRE', max_length=50)
    nombre_dos = forms.CharField(label='SEGUNDO NOMBRE', max_length=50)
    apellido_paterno = forms.CharField(label='APELLIDO PATERNO', max_length=50)
    apellido_materno = forms.CharField(label='APELLIDO MATERNO', max_length=50)
    sexo = forms.ChoiceField(label='SEXO',choices=(('F', 'Femenino'),('M', 'Masculino')),)
    direcion = forms.CharField(label='DIRECION', max_length=100)
    # fechNacimiento = forms.DateField('fecha de naciemiento',default=timezone.now)