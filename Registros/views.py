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
from django.core import serializers
from django.http import HttpResponse

#############################################
############# VISTA PRINCIPAL   #############
#############################################
class IndexView(generic.ListView):
	template_name='registros/index.html'
	context_object_name='all_albums'
	def get_queryset(self):
		return Paciente.objects.all()

################################################
############# BUSQUEDA DE PACIENTE #############
################################################
class BusquedaView(generic.ListView):
    template_name='registros/buscar.html' 
    model= Paciente

class BusquedaAjaxView(generic.TemplateView):
    def get(self,request,*args,**kwargs):
        var=request.GET['id']
        if var!='':
            new = Paciente.objects.filter(Q(nombre1__contains=var) | Q(apellPadre__contains=var) | Q(cedula__contains=var))
        else:
            new = {}
        data = serializers.serialize('json',new,fields=('cedula','nombre1','apellPadre','fech_actualizado'))
        return HttpResponse(data,content_type='application/json')

################################################
############# CREACION DE PACIENTE #############
################################################

class Crear_paciente(CreateView):
    model = Paciente
    fields='__all__'
    template_name='registros/paciente_form.html'
    success_url = '/registros/buscar'
    success_message = 'Paciente creado correctamente'


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


##########################################################
##################FORMULARIOS PARA ECOGRAFIA##############
##########################################################

def get_initial_pri(self, **kwargs):
    parametro = self.kwargs.get('ident',None)
    paciente = Paciente.objects.get(pk=parametro)
    return {'paciente':paciente,}

def get_context_data_pri(self, nomclass,**kwargs):
    parametro = self.kwargs.get('ident',None)
    paciente = Paciente.objects.get(pk=parametro)
    context = super(nomclass, self).get_context_data(**kwargs) 
    context['paciente']= paciente
    print(context)
    return context

class EcomamaCreate(CreateView):
    model = analisisMamas
    fields='__all__'
    template_name='registros/ecomamanew.html'
    context_object_name='datos'
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        return get_context_data_pri(self,EcomamaCreate, **kwargs)

class EcoabdomenCreate(CreateView):
    model=analisisAbdominal
    fields='__all__'
    template_name='registros/ecoabdomennew.html'
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        return get_context_data_pri(self,EcoabdomenCreate, **kwargs)

class EcoobstetricoCreate(CreateView):
    model=analisisObstetrico
    fields='__all__'
    template_name='registros/ecoobstericonew.html'
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        return get_context_data_pri(self,EcoobstetricoCreate, **kwargs)

class EcorenalCreate(CreateView):
    model=ecografiaRenal
    fields='__all__'
    template_name='registros/ecorenalnew.html'
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        return get_context_data_pri(self,EcorenalCreate, **kwargs)

class EcoginecologiaCreate(CreateView):
    model=ecografiaginecologico
    fields='__all__'
    template_name='registros/ecoginecologianew.html'
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        return get_context_data_pri(self,EcoginecologiaCreate, **kwargs)

class EcotesticularCreate(CreateView):
    model=ecografiatesticular
    fields='__all__'
    template_name='registros/ecotesticularnew.html'
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        return get_context_data_pri(self,EcotesticularCreate, **kwargs)

class ListDiagnostico(DetailView):
    model = Paciente
    template_name='registros/diagnostico_list.html'
    def get_context_data(self,**kwargs):
        context = super(ListDiagnostico, self).get_context_data(**kwargs) 
        print(context)
        return context




