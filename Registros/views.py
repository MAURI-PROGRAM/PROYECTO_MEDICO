from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Paciente
# Create your views here.

def index(request):
	all_pacientes=Paciente.objects.all()
	cotexto={'all_pacientes' : all_pacientes}
	return render(request,'registros/index.html',cotexto)



def detail(request,id_p):
	try:
		paciente=Paciente.objects.get(pk=id_p)
		cotexto={'paciente' : paciente}
	except Paciente.DoesNotExist:
		raise Http404("Album no existe")
	return render(request,'registros/detail.html',cotexto)