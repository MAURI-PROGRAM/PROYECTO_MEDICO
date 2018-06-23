from django.db import models
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
	fechNacimiento=models.DateTimeField('fecha de naciemiento',default=timezone.now)
	lugarNacimiento=models.CharField(max_length=100,verbose_name='LUGAR DE NACIMIENTO')
	nacionalidad=models.CharField(max_length=100,verbose_name='NACIONALIDAD')
	grupoCultural=models.CharField(max_length=100,verbose_name='GRUPO CULTURAL')
	estadoCivil=models.CharField(max_length=3,choices=(('SOL', 'Soltero'),('CAS', 'Casado'),('DIV', 'Divorciado'),('VIU', 'Viudo'),('UNL', 'Unión libre')))
	instruccion=models.CharField(max_length=100,verbose_name='INSTRUCION EDUCATIVA')
	fechaAdmision=models.DateTimeField(default=timezone.now,verbose_name='FECHA DE ADMISION')
	ocupacion=models.DateTimeField(default=timezone.now,verbose_name='OCUPACION')
	empresa=models.CharField(max_length=100,verbose_name='EMPRESA')
	