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
	fech_creado=models.DateTimeField(auto_now_add=True,verbose_name='FECHA DE ADMISION')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')

	def __str__(self):
		return self.apellPadre+' '+self.apellMadre+' '+self.apellPadre+' '+self.nombre1+' '+self.nombre2


class Diagnostico(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	precion_arterial=models.CharField(max_length=30,verbose_name='PRESION ARTERIAL')
	temperatura=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='TEMPERATURA(°C)')
	peso=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='PASO(KG)')
	evolucion=models.CharField(max_length=300,verbose_name='EVOLUCION')
	pulso=models.CharField(max_length=20,verbose_name='PULSO')
	saturacion_oxigeno=models.CharField(max_length=20,verbose_name='SATURACION DE OXIGENO')
	talla=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='ESTATURA')
	idx=models.CharField(max_length=100,verbose_name='IDX')
	exmenes=models.CharField(max_length=200,verbose_name='EXAMENES')
	motivo=models.CharField(max_length=300,verbose_name='MOTIVO')
	fechaDiagnostico=models.DateTimeField(auto_now_add=True,verbose_name='FECHA DE DIAGNOSTICO')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')