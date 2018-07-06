from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Paciente
# Create your views here.

def index(request):
	all_pacientes=Paciente.objects.all()
	cotexto={'all_pacientes' : all_pacientes}
	return render(request,'registros/index.html',cotexto)

def detail(request,id_p):
	paciente=get_object_or_404(Paciente,pk=id_p)
	cotexto={'paciente' : paciente}
	return render(request,'registros/detail.html',cotexto)