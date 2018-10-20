from django import forms
# from .forms import Paciente
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
    # fechNacimiento=forms.DateField('fecha de naciemiento',default=timezone.now)
    lugarNacimiento=forms.CharField(max_length=100,label='LUGAR DE NACIMIENTO')
    nacionalidad=forms.CharField(max_length=100,label='NACIONALIDAD')
    grupoCultural=forms.CharField(max_length=100,label='GRUPO CULTURAL')
    estadoCivil=forms.ChoiceField(label='ESTADO CIVIL',choices=(('SOL', 'Soltero'),('CAS', 'Casado'),('DIV', 'Divorciado'),('VIU', 'Viudo'),('UNL', 'Unión libre')))
    instruccion=forms.CharField(max_length=100,label='INSTRUCION EDUCATIVA')
    ocupacion=forms.CharField(max_length=100,label='OCUPACION')
    empresa=forms.CharField(max_length=100,label='EMPRESA')
    tipo_sangre=forms.CharField(max_length=100,label='TIPO DE SANGRE')
    tipo_seguro=forms.CharField(max_length=100,label='TIPO DE SEGURIDAD')
    telefono=forms.CharField(max_length=9,label='TELEFONO')
    celular=forms.CharField(max_length=10,label='CELULAR')
    correo=forms.EmailField(label='CORREO')
    pariente=forms.CharField(max_length=100,label='NOMBRE PARIENTE')
    parentesco=forms.CharField(max_length=100,label='PARENTESCO')
    telefono_pariente=forms.CharField(max_length=9,label='TELEFONO PARIENTE')
    celular_pariente=forms.CharField(max_length=10,label='CELULAR PARIENTE')
    # foto=forms.ImageField(upload_to='fotos')