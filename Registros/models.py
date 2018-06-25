from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta
from django.utils.timezone import now
# Create your models here.

class Paciente(models.Model):
	cedula=models.CharField(max_length=13,unique=True,verbose_name='CEDULA DE IDENTIDAD')
	nombre1=models.CharField(max_length=50,verbose_name='PRIMER NOMBRE')
	nombre2=models.CharField(max_length=50,verbose_name='SEGUNDO NOMBRE')
	apellPadre=models.CharField(max_length=50,verbose_name='PRIMER APELLIDO')
	apellMadre=models.CharField(max_length=50,verbose_name='SEGUNDO APELLIDO')
	sexo=models.CharField(max_length=2,choices=(('F', 'Femenino'),('M', 'Masculino'),))
	direccion=models.CharField(max_length=100,verbose_name='DIRECCION DOMICILIARIA')
	fechNacimiento=models.DateField('fecha de naciemiento',default=timezone.now)
	lugarNacimiento=models.CharField(max_length=100,verbose_name='LUGAR DE NACIMIENTO')
	nacionalidad=models.CharField(max_length=100,verbose_name='NACIONALIDAD')
	grupoCultural=models.CharField(max_length=100,verbose_name='GRUPO CULTURAL')
	estadoCivil=models.CharField(max_length=3,choices=(('SOL', 'Soltero'),('CAS', 'Casado'),('DIV', 'Divorciado'),('VIU', 'Viudo'),('UNL', 'Unión libre')))
	instruccion=models.CharField(max_length=100,verbose_name='INSTRUCION EDUCATIVA')
	fechaAdmision=models.DateTimeField(default=timezone.now,verbose_name='FECHA DE ADMISION')
	ocupacion=models.CharField(max_length=100,verbose_name='OCUPACION')
	empresa=models.CharField(max_length=100,verbose_name='EMPRESA')
	tipo_sangre=models.CharField(max_length=100,verbose_name='TIPO DE SANGRE')
	tipo_seguro=models.CharField(max_length=100,verbose_name='TIPO DE SEGURIDAD')
	telefono=models.CharField(max_length=9,verbose_name='TELEFONO DEL PACIENTE')
	celular=models.CharField(max_length=10,verbose_name='CELULAR DEL PACIENT')
	correo=models.EmailField(verbose_name='CORREO DEL PACIENT')
	pariente=models.CharField(max_length=100,verbose_name='NOMBRE PARIENTE')
	parentesco=models.CharField(max_length=100,verbose_name='PARENTESCO')
	telefono_pariente=models.CharField(max_length=9,verbose_name='TELEFONO DEL REFERIDO')
	celular_pariente=models.CharField(max_length=10,verbose_name='CELULAR DEL REFERIDO')
	foto=models.ImageField(upload_to='fotos')