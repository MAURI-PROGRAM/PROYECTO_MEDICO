from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta
from django.utils.timezone import now
from django.urls import reverse
# Create your models here.

class Paciente(models.Model):
	cedula=models.CharField(max_length=13,unique=True,verbose_name='Cedula de indentidad')
	nombre1=models.CharField(max_length=50,verbose_name='Primer nombre')
	nombre2=models.CharField(max_length=50,verbose_name='Segundo nombre')
	apellPadre=models.CharField(max_length=50,verbose_name='Apellido paterno')
	apellMadre=models.CharField(max_length=50,verbose_name='Apellido materno')
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
	telefono=models.CharField(max_length=9,verbose_name='Telefono del paciente')
	celular=models.CharField(max_length=10,verbose_name='Celular del paciente')
	correo=models.EmailField(verbose_name='Correo del paciente')
	pariente=models.CharField(max_length=100,verbose_name='NOMBRE PARIENTE')
	parentesco=models.CharField(max_length=100,verbose_name='Parentesco')
	telefono_pariente=models.CharField(max_length=9,verbose_name='Telefono del pariente')
	celular_pariente=models.CharField(max_length=10,verbose_name='Celular del referido')
	foto=models.ImageField(upload_to='fotos', null=True,blank=True)
	fech_creado=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de admision')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')

	def get_absolute_url(self):
		return reverse('registros:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.apellPadre+' '+self.apellMadre+' '+self.nombre1+' '+self.nombre2

class Diagnostico(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	precion_arterial=models.CharField(max_length=30,verbose_name='PRESION ARTERIAL')
	temperatura=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='TEMPERATURA(°C)')
	peso=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='PESO(KG)')
	evolucion=models.CharField(max_length=300,verbose_name='EVOLUCION')
	pulso=models.CharField(max_length=20,verbose_name='PULSO')
	saturacion_oxigeno=models.CharField(max_length=20,verbose_name='SATURACION DE OXIGENO')
	talla=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='ESTATURA')
	idx=models.CharField(max_length=100,verbose_name='IDX')
	exmenes=models.CharField(max_length=200,verbose_name='EXAMENES')
	motivo=models.CharField(max_length=300,verbose_name='MOTIVO')
	fechaDiagnostico=models.DateTimeField(auto_now_add=True,verbose_name='FECHA DE DIAGNOSTICO')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')

class farmacoterapia(models.Model):
	diagnostico= models.ForeignKey(Diagnostico, on_delete=models.CASCADE,verbose_name='Diagnostico')
	farmaco=models.CharField(max_length=300,verbose_name='Farmaco')
	adminitracion=models.CharField(max_length=300,verbose_name='Administracion')
	comentario=models.CharField(max_length=300,verbose_name='Comentario')

class analisisMamas(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	tegGlandularizq=models.CharField(max_length=20,choices=(('HOMOGENEO', 'Homogéneo'),('HETEROGENEO', 'Heterogéneo')))
	infotegGlandularizq=models.CharField(max_length=100)
	tegGlandularder=models.CharField(max_length=20,choices=(('HOMOGENEO', 'Homogéneo'),('HETEROGENEO', 'Heterogéneo')))
	infotegGlandularder=models.CharField(max_length=100)
	bordesizq=models.CharField(max_length=20,choices=(('REGULAR', 'Regulares'),('IRREGULAR', 'Irregulares')))
	bordesder=models.CharField(max_length=20,choices=(('REGULAR', 'Regulares'),('IRREGULAR', 'Irregulares')))
	ecogenidadizq=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('DISMINUIDA', 'Disminuida'),('AUMENTADA', 'Aumentada')))
	ecogenidadder=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('DISMINUIDA', 'Disminuida'),('AUMENTADA', 'Aumentada')))
	tejGrasoizq=models.CharField(max_length=20,choices=(('BUENA', 'Buena Cantidad'),('POCA', 'Poca Cantidad')))
	tejGrasoder=models.CharField(max_length=20,choices=(('BUENA', 'Buena Cantidad'),('POCA', 'Poca Cantidad')))
	imgExpansivasizq=models.CharField(max_length=20,choices=(('NO', 'No'),('QUISTICA', 'Quísticas'),('SOLIDA', 'Sólidas')))
	imgExpansivasder=models.CharField(max_length=20,choices=(('NO', 'No'),('QUISTICA', 'Quísticas'),('SOLIDA', 'Sólidas')))
	horarioizq=models.CharField(max_length=400,verbose_name='HORARIO')
	horarioder=models.CharField(max_length=400,verbose_name='HORARIO')
	descripcionizq=models.CharField(max_length=500,verbose_name='DESCRIPCION')
	descripcionder=models.CharField(max_length=500,verbose_name='DESCRIPCION')
	observaciones=models.CharField(max_length=500,verbose_name='OBSERBACIONES')
	presuncion=models.CharField(max_length=800,verbose_name='PRESIÓN DIAGNÓSTICA')
	fech_analisismamas=models.DateTimeField(auto_now_add=True,verbose_name='FECHA DE ADMISION')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')
	def get_absolute_url(self):
		return reverse('registros:ecografia')

class analisisAbdominal(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	movilidad_higado=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('ANORMAL', 'Anormal')))
	bordes_higado=models.CharField(max_length=20,choices=(('REGULAR', 'Regulares'),('IRREGULAR', 'Irregulares')))
	dimension_higado=models.CharField(max_length=20,choices=(('NORMALES', 'Normales'),('OTROS', 'Otros')))
	parenquima_higado=models.CharField(max_length=20,choices=(('HOMOGENEO', 'Homogéneo'),('HETEROGENEO', 'Heterogéneo')))
	ecogenicidad_higado=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('DISMINUIDA', 'Disminuida'),('AUMENTADA', 'Aumentada')))
	imgExpansivas_higado=models.CharField(max_length=2,choices=(('NO', 'No'),('SI', 'Si')))
	dilatacionVilar_higado=models.CharField(max_length=2,choices=(('NO', 'No'),('SI', 'Si')))
	coledoco_higado=models.CharField(max_length=200,verbose_name='COLEDOCO')
	forma_vesicula=models.CharField(max_length=200,verbose_name='FORMA')
	paredes_vesicula=models.CharField(max_length=20,choices=(('REGULAR', 'Regulares'),('IRREGULAR', 'Irregulares')))
	contenidoanecoico_vesicula=models.CharField(max_length=2,choices=(('NO', 'No'),('SI', 'Si')))
	calculointerno_vesicula=models.CharField(max_length=200,verbose_name='CALCULOS INTERNOS')
	diametrotransverso_vesicula=models.CharField(max_length=200,verbose_name='DIAMETRO TRANSVERSOS')
	ecogenicidad_pancreas=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('ANORMAL', 'Anormal')))
	medidas_pancreas=models.CharField(max_length=200,verbose_name='MEDIDAS')
	ecogenidad_bazo=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('ANORMAL', 'Anormal')))
	medidas_bazo=models.CharField(max_length=200,verbose_name='MEDIDAS')
	aorta=models.CharField(max_length=200,verbose_name='CALIBRES')
	liquido_abdominal=models.CharField(max_length=2,choices=(('NO', 'No'),('SI', 'Si')))
	observaciones=models.CharField(max_length=200,verbose_name='OBSERBACIONES')
	presuncion_diagnostico=models.CharField(max_length=500,verbose_name='PRESUNCION_DIAGNOSTICA')
	fech_analisisabdomen=models.DateTimeField(auto_now_add=True,verbose_name='FECHA DE ADMISION')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')

	def get_absolute_url(self):
		return reverse('registros:ecografia')

	def __str__(self):
		return str(self.paciente)+' '+str(self.fech_analisisabdomen)

class analisisObstetrico(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	numero=models.PositiveSmallIntegerField(default=1)
	situacion=models.CharField(max_length=20,choices=(('LONGITUDINAL', 'Longitudinal'),('TRANSVERSAL', 'TRANSVERSAL'),('OBLICUA', 'Oblicua')))
	presentacion=models.CharField(max_length=20,choices=(('CEFALICO', 'Cefalico'),('PODALICO', 'Podalico'),('OTROS', 'Otros')))
	dorso=models.CharField(max_length=20,choices=(('IZQUIERDA', 'Izquierda'),('DERECHA', 'Derecha'),('ANTERIOR', 'Anterior'),('POSTERIOR', 'Posterior')))
	dbp=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='DBP(mm)')
	lf=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='LF(mm)')
	sg=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='SG(mm)')
	lcn=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='LCN(mm)')
	columnaVertebral=models.CharField(max_length=20,choices=(('PRESENTE', 'Presente'),('CAMARA GASTRICA', 'Camara Gástrica')))
	riñon=models.CharField(max_length=20,choices=(('PRESENTE', 'Presente'),('VEJIGA', 'Vejiga')))
	actividadCardiaca=models.CharField(max_length=20,choices=(('PRESENTE', 'Presente'),('OTRO', 'Otro')))
	movimientoFetal=models.CharField(max_length=20,choices=(('PRESENTE', 'Presente'),('OTRO', 'Otro')))
	descrionFetal=models.CharField(max_length=300,verbose_name='DESCRIPCION')
	localizacionPlacenta=models.CharField(max_length=20,choices=(('FUNDICA', 'Fúndica'),('ANTERIOR', 'Anterior'),('POSTERIOR', 'Posterior'),('OTROS', 'Otras Posiciones')))
	grado=models.CharField(max_length=20,choices=(('0', '0'),('I', 'I'),('II', 'II'),('III', 'III')))
	espesorplacenta=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Espesor placentario(mm)')
	descrionplacenta=models.CharField(max_length=300,verbose_name='DESCRIPCION')
	volumen=models.CharField(max_length=20,choices=(('NORMAL', 'Fúndica'),('OLIGOHIDRAMNIOS', 'Oligohidramnios'),('POLIHIDRAMNIOS', 'Polihidramnios')))
	descrionamniotica=models.CharField(max_length=300,verbose_name='DESCRIPCION')
	circulardecordon=models.CharField(max_length=2,choices=(('NO', 'No'),('SI', 'Si')))
	observaciones=models.CharField(max_length=300,verbose_name='OBSERVACIONES')
	presuncionDiagnostico=models.CharField(max_length=500,verbose_name='PRESUNCION_DIAGNOSTICA:El estudio Ultrasonografico es compatible con:')
	fech_analisisobstetrico=models.DateTimeField(auto_now_add=True,verbose_name='FECHA ANALISIS OBSTETRICO')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')
	
	def get_absolute_url(self):
		return reverse('registros:ecografia')

	def __str__(self):
		return str(self.paciente)+' '+str(self.fech_analisisobstetrico)

class ecografiaRenal(models.Model): 
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	motivoExamen=models.CharField(max_length=500,verbose_name='MOTIVO DEL EXAMEN')
	movilidad_riñonder=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('ANORMAL', 'Anormal')))
	movilidad_riñonizq=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('ANORMAL', 'Anormal')))
	ecogenicidad_riñonder=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('AUMENTADA', 'Aumentada'),('DISMINUIDA', 'Disminuida')))
	ecogenicidad_riñonizq=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('AUMENTADA', 'Aumentada'),('DISMINUIDA', 'Disminuida')))
	medidalongitud_riñonder=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Longitudinal(mm)')
	medidalongitud_riñonizq=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Longitudinal(mm)')
	medidaparenquima_riñonder=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Parenquima(mm)')
	medidaparenquima_riñonizq=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Parenquima(mm)')
	imgExpansivas_solidasder=models.CharField(max_length=2,choices=(('NO', 'No'),('SI', 'Si')))
	imgExpansivas_solidasizq=models.CharField(max_length=2,choices=(('NO', 'No'),('SI', 'Si')))
	imgExpansivas_quisticasder=models.CharField(max_length=2,choices=(('NO', 'No'),('SI', 'Si')))
	imgExpansivas_quisticasizq=models.CharField(max_length=2,choices=(('NO', 'No'),('SI', 'Si')))
	hidronefrosisder=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Hidronefrosis(mm)')
	hidronefrosisizq=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Hidronefrosis(mm)')
	microlitiasisder=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Microlitiasis(mm)')
	microlitiasisizq=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Microlitiasis(mm)')
	calculo_der=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Calculos(mm)')
	calculo_izq=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Calculos(mm)')
	descripcionder=models.CharField(max_length=500,verbose_name='DESCRIPCION')
	descripciondizq=models.CharField(max_length=500,verbose_name='DESCRIPCION')
	replecion=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('MINIMO', 'Minimo'),('EXCESIVA', 'Excesova')))
	paredes=models.CharField(max_length=20,choices=(('NORMAL', 'Normal'),('DELGADA', 'Delgada'),('ENGROSADA', 'Engrosada')))
	contenidoAnecoico=models.CharField(max_length=200,verbose_name='Conteniso anecoico')
	imgExpansivasvegiga=models.CharField(max_length=200,verbose_name='Imagenes expansivas')
	calculointerior=models.CharField(max_length=200,verbose_name='Calculos en su interior')
	volpremicional=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='volpremicional(cc)')
	volpostmiccional=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='volpostmiccional(cc)')
	retencion=models.DecimalField(max_digits=10, decimal_places=2,verbose_name='retencion(cc)')
	descripcionveg=models.CharField(max_length=500,verbose_name='DESCRIPCION')
	observaciones=models.CharField(max_length=200,verbose_name='OBSERBACIONES')
	presuncionDiagnostico=models.CharField(max_length=500,verbose_name='PRESUNCION_DIAGNOSTICA')
	fech_informe=models.DateTimeField(auto_now_add=True,verbose_name='FECHA INFORME ECOGRAFICO RENAL')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')

	def get_absolute_url(self):
		return reverse('registros:ecografia')

	def __str__(self):
		return str(self.paciente)+' '+str(self.fech_informe)


class ecografiaginecologico(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	motivoExamen=models.CharField(max_length=500,verbose_name='MOTIVO DEL EXAMEN')
	posicionUtero=models.CharField(max_length=20,choices=(('ANTEVERSO', 'Anteverso'),('CENTRAL', 'Central'),('RETROVRSO', 'Retroverso')))
	contornoUtero=models.CharField(max_length=100,verbose_name='CONTORNO')
	ecoestructura=models.CharField(max_length=100,verbose_name='ESTRUCTURA')
	medidas=models.CharField(max_length=100,verbose_name='MEDIDAS')
	endometrio=models.CharField(max_length=20,choices=(('MENSTRUAL', 'Menstrual'),('PROLIF', 'Prolif.'),('PERIOF', 'Periof.'),('SECRET', 'Secret')))
	descripcion=models.CharField(max_length=500,verbose_name='DESCRIPCION')
	anexodermedidas=models.CharField(max_length=200,verbose_name='DESCRIPCION')
	anexodermasas=models.CharField(max_length=20,choices=(('NO', 'No'),('QUISTE', 'Quiste.'),('SOLIDAS', 'Solidas.')))
	anexoderdescripcion=models.CharField(max_length=300,verbose_name='DESCRIPCION')
	anexoizqmedidas=models.CharField(max_length=200,verbose_name='DESCRIPCION')
	anexoizqmasas=models.CharField(max_length=20,choices=(('NO', 'No'),('QUISTE', 'Quiste.'),('SOLIDAS', 'Solidas.')))
	anexoizqdescripcion=models.CharField(max_length=300,verbose_name='DESCRIPCION')
	liquidolibre=models.CharField(max_length=20,choices=(('NO', 'No'),('ESCASO', 'Escaso.'),('MODERADO', 'Moderado.'),('ABUNDANTE', 'Abundante.')))
	observacion=models.CharField(max_length=500,verbose_name='OBSERVACION')
	presuncionDiagnostico=models.CharField(max_length=500,verbose_name='PRESUNCION_DIAGNOSTICA')
	fech_informe=models.DateTimeField(auto_now_add=True,verbose_name='FECHA INFORME ECOGRAFICO GINECOLOGICO')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')

	def get_absolute_url(self):
		return reverse('registros:ecografia')

class ecografiatesticular(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	motivoExamen=models.CharField(max_length=500,verbose_name='MOTIVO DEL EXAMEN')
	testiculoder=models.CharField(max_length=300,verbose_name='DERECHO')
	epididimoder=models.CharField(max_length=300,verbose_name='EPIDIDIMODER')
	liqescrotalder=models.CharField(max_length=300,verbose_name='LIQUIDO INTRA ESCROTAL')
	testiculoizq=models.CharField(max_length=300,verbose_name='IZQUIERDO')
	epididimoizq=models.CharField(max_length=300,verbose_name='EPIDIDIMODER')
	liqescrotalizq=models.CharField(max_length=300,verbose_name='LIQUIDO INTRA ESCROTAL')
	observacion=models.CharField(max_length=500,verbose_name='OBSERVACION')
	presuncionDiagnostico=models.CharField(max_length=500,verbose_name='PRESUNCION_DIAGNOSTICA')
	fech_informe=models.DateTimeField(auto_now_add=True,verbose_name='FECHA INFORME ECOGRAFICO TESTICULAR')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')

	def get_absolute_url(self):
		return reverse('registros:ecografia')

	def __str__(self):
		return str(self.paciente)+' '+str(self.fech_informe)


class ecografiaprostata(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	repelecion=models.CharField(max_length=20,choices=(('BUENA', 'Buena'),('VACUA', 'Vacua'),('POCA', 'Poca')))
	paredes=models.CharField(max_length=20,choices=(('REGULARES', 'Regulares'),('IRREGULARES', 'Irregulares'),('DELGADA', 'Delgada'),('ENGROSADA', 'Engrosada')))
	contenidoanecoico=models.CharField(max_length=50,verbose_name='Contenido Anecoico')
	imgExpansivas=models.CharField(max_length=50,verbose_name='Imagenes expansivas')
	calculointerior=models.CharField(max_length=50,verbose_name='Cálculo en su interior')
	volpremiccional=models.CharField(max_length=200,verbose_name='Vol. Pre-miccional')
	descripcion=models.CharField(max_length=200,verbose_name='Descripcion/Otros')
	bordes=models.CharField(max_length=100,verbose_name='Bordes')
	dimensiones=models.CharField(max_length=400,verbose_name='Dimensiones')
	volumen=models.CharField(max_length=100,verbose_name='Volumen')
	ecoestructura=models.CharField(max_length=100,verbose_name='Bordes')
	observacion=models.CharField(max_length=500,verbose_name='OBSERVACION')
	presuncionDiagnostico=models.CharField(max_length=500,verbose_name='PRESUNCION_DIAGNOSTICA')
	fech_informe=models.DateTimeField(auto_now_add=True,verbose_name='FECHA INFORME ECOGRAFICO PROSTATA')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='FECHA DE ACTUALIZACION')

	def get_absolute_url(self):
		return reverse('registros:ecografia')

	def __str__(self):
		return str(self.paciente)+' '+str(self.fech_informe)


class desintometria(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	encabezado = models.CharField(max_length=50,verbose_name='Encabezado')
	observaciones = models.CharField(max_length=10000,verbose_name='Observaciones')
	fech_informe=models.DateTimeField(auto_now_add=True,verbose_name='')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='')

class rayosx(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	encabezado = models.CharField(max_length=50,verbose_name='Encabezado')
	observaciones = models.CharField(max_length=10000,verbose_name='Observaciones')
	fech_informe=models.DateTimeField(auto_now_add=True,verbose_name='')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='')

class terapias(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	encabezado = models.CharField(max_length=50,verbose_name='Encabezado')
	observaciones = models.CharField(max_length=10000,verbose_name='Observaciones')
	fech_informe=models.DateTimeField(auto_now_add=True,verbose_name='')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='')

class ekg(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,verbose_name='PACIENTE')
	encabezado = models.CharField(max_length=50,verbose_name='Encabezado')
	observaciones = models.CharField(max_length=10000,verbose_name='Observaciones')
	fech_informe=models.DateTimeField(auto_now_add=True,verbose_name='')
	fech_actualizado=models.DateTimeField(auto_now=True,verbose_name='')