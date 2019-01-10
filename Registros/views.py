from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
import datetime
from django.views.generic import ListView,DetailView
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from .models import Paciente,Diagnostico,analisisMamas,analisisAbdominal,analisisObstetrico,ecografiaRenal,ecografiaginecologico,ecografiatesticular
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(generic.ListView):
	template_name='registros/index.html'
	context_object_name='all_albums'
	def get_queryset(self):
		return Paciente.objects.all()

class BuscarView(generic.ListView):
    template_name='registros/busqueda.html'
    context_object_name='pacientes_encontrados'
    def get_queryset(self,**kwargs):
        var = self.kwargs.get('nom','')
        return Paciente.objects.filter(Q(nombre1__contains=var) | Q(apellPadre__contains=var) | Q(cedula__contains=var))

from django.core import serializers
from django.http import HttpResponse
class BusquedaAjaxView(generic.TemplateView):
    def get(self,request,*args,**kwargs):
        var=request.GET['id']
        if var!='':
            new = Paciente.objects.filter(Q(nombre1__contains=var) | Q(apellPadre__contains=var) | Q(cedula__contains=var))
        else:
            new = {}

        data = serializers.serialize('json',new,fields=('cedula','nombre1','apellPadre','fech_actualizado'))
        return HttpResponse(data,content_type='application/json')


class IngresoView(generic.ListView):
    template_name='registros/paciente.html'
    context_object_name='datos'
    def get_queryset(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        return Paciente.objects.get(pk=parametro)


class EcoView(generic.ListView):
    template_name='registros/ecografias.html'
    context_object_name='datos'
    def get_queryset(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        return Paciente.objects.get(pk=parametro)

class EcomamaCreate(CreateView):
    model = analisisMamas
    fields='__all__'
    template_name='registros/ecomamanew.html'
    def get_initial(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        paciente = Paciente.objects.get(pk=parametro)
        return {
            'paciente':paciente,
        }

class EcoabdomenCreate(CreateView):
    model=analisisAbdominal
    fields='__all__'
    template_name='registros/ecoabdomennew.html'
    def get_initial(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        paciente = Paciente.objects.get(pk=parametro)
        return {
            'paciente':paciente,
        }

class EcoobstetricoCreate(CreateView):
    model=analisisObstetrico
    fields='__all__'
    template_name='registros/ecoobstericonew.html'
    def get_initial(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        paciente = Paciente.objects.get(pk=parametro)
        return {
            'paciente':paciente,
        }

class Crear_paciente(CreateView):
    model = Paciente
    fields='__all__'
    template_name='registros/paciente_form.html'
    success_url = '/registros/buscar'
    success_message = 'Paciente creado correctamente'


class EcorenalCreate(CreateView):
    model=ecografiaRenal
    fields='__all__'
    template_name='registros/ecorenalnew.html'
    def get_initial(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        paciente = Paciente.objects.get(pk=parametro)
        return {
            'paciente':paciente,
        }

class EcoginecologiaCreate(CreateView):
    model=ecografiaginecologico
    fields='__all__'
    template_name='registros/ecoginecologianew.html'
    def get_initial(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        paciente = Paciente.objects.get(pk=parametro)
        return {
            'paciente':paciente,
        }


class EcotesticularCreate(CreateView):
    model=ecografiatesticular
    fields='__all__'
    template_name='registros/ecotesticularnew.html'
    def get_initial(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        paciente = Paciente.objects.get(pk=parametro)
        return {
            'paciente':paciente,
        }


def get_info(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
        	form = PacienteForm()
        	return render(request, 'registros/form1.html', {'form': form})
    else:
        form = PacienteForm()
    return render(request, 'registros/form1.html', {'form': form})


class paciente_new(ListView):
    template_name = 'registros/diagnostivo_list.html'
    def get_queryset(self):
        self.paciente = get_object_or_404(Paciente, name=self.kwargs['paciente'])
        return Diagnostico.objects.filter(paciente=self.paciente)


class BusquedaView(generic.ListView):
    template_name='registros/buscar.html' 
    model= Paciente



