from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
import datetime
from django.views.generic import ListView,DetailView
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from .models import Paciente,Diagnostico,analisisMamas,analisisAbdominal,analisisObstetrico,ecografiaRenal,ecografiaginecologico,ecografiatesticular,farmacoterapia,ekg,terapias,rayosx,desintometria
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core import serializers
from django.http import HttpResponse
from extra_views import CreateWithInlinesView,InlineFormSetFactory
#############################################
############ crear nuevo diagnostico#########
#############################################


def get_initial_pri(self, **kwargs):
    parametro = self.kwargs.get('ident',None)
    paciente = Paciente.objects.get(pk=parametro)
    return {'paciente':paciente,}

def get_context_data_pri(self, nomclass,extra,**kwargs):
    parametro = self.kwargs.get('ident',None)
    paciente = Paciente.objects.get(pk=parametro)
    context = super(nomclass, self).get_context_data(**kwargs) 
    context['paciente']= paciente
    context['extrainfo'] = extra
    print(context)
    return context



class ItemInline(InlineFormSetFactory):
    model = farmacoterapia
    fields = ['farmaco', 'adminitracion', 'comentario']
    factory_kwargs = {'extra':7, 'max_num': None,
                      'can_order': False, 'can_delete': True}
    formset_kwargs = {'auto_id': 'my_id_%s','save_as_new': True}

class CreateOrderView(CreateWithInlinesView):
    model = Diagnostico
    inlines = [ItemInline]
    fields = ['paciente', 'precion_arterial', 'temperatura','peso','evolucion','pulso','saturacion_oxigeno','talla','idx','exmenes','motivo','encargado']
    template_name = 'registros/nuevo_diagnostico.html'
    inlines_names = ['Items', 'Tags']

    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return '/registros/paciente/listar_diagnostico/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        paciente = Paciente.objects.get(pk=parametro)
        return {'paciente':paciente,}
    def get_context_data(self, **kwargs):
        parametro = self.kwargs.get('ident',None)
        paciente = Paciente.objects.get(pk=parametro)
        context = super(CreateOrderView, self).get_context_data(**kwargs)
        extra={'title':'Diagnosticos','page':'Nuevo Diagnostico'}
        context['paciente']= paciente
        context['extrainfo'] = extra
        print(context)
        return context


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

def get_context_data_pri(self, nomclass,extra,**kwargs):
    parametro = self.kwargs.get('ident',None)
    paciente = Paciente.objects.get(pk=parametro)
    context = super(nomclass, self).get_context_data(**kwargs) 
    context['paciente']= paciente
    context['extrainfo'] = extra
    print(context)
    return context

class EcomamaCreate(CreateView):
    model = analisisMamas
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    context_object_name='datos'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Ecografia Mamas','page':'Ecografia Mamas'}
        return get_context_data_pri(self,EcomamaCreate,extrainfo, **kwargs)

class EcoabdomenCreate(CreateView):
    model=analisisAbdominal
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Ecografia abdominal','page':'Ecografia abdominal'}
        return get_context_data_pri(self,EcoabdomenCreate,extrainfo, **kwargs)

class EcoobstetricoCreate(CreateView):
    model=analisisObstetrico
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Ecografia Obstetrico','page':'Ecografia Obstetrico'}
        return get_context_data_pri(self,EcoobstetricoCreate,extrainfo, **kwargs)

class EcorenalCreate(CreateView):
    model=ecografiaRenal
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Ecografia Renal','page':'Ecografia Renal'}
        return get_context_data_pri(self,EcorenalCreate,extrainfo, **kwargs)

class EcoginecologiaCreate(CreateView):
    model=ecografiaginecologico
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Ecografia Ginecologia','page':'Ecografia Ginecologia'}
        return get_context_data_pri(self,EcoginecologiaCreate,extrainfo, **kwargs)

class EcotesticularCreate(CreateView):
    model=ecografiatesticular
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Ecografia Testicular','page':'Ecografia Testicular'}
        return get_context_data_pri(self,EcotesticularCreate,extrainfo, **kwargs)


############################################################
##################   OTROS FORMULARIOS #####################
############################################################

class DesintometriaCreate(CreateView):
    model = desintometria
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Desintometria','page':'Desintometria'}
        return get_context_data_pri(self,DesintometriaCreate,extrainfo, **kwargs)

class TerapiaCreate(CreateView):
    model = terapias
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Terapias','page':'Terapias'}
        return get_context_data_pri(self,TerapiaCreate,extrainfo, **kwargs)

class EkgCreate(CreateView):
    model = ekg
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Ekg','page':'Ekg'}
        return get_context_data_pri(self,EkgCreate,extrainfo, **kwargs)


class RayosxCreate(CreateView):
    model = rayosx
    fields='__all__'
    template_name='registros/base_ecografias_form.html'
    def get_success_url(self):
        parametro = self.kwargs.get('ident',None)
        return 'listar/{0}'.format(parametro)
    def get_initial(self, **kwargs):
        return get_initial_pri(self, **kwargs)
    def get_context_data(self, **kwargs):
        extrainfo={'title':'Rayos X','page':'Rayos X'}
        return get_context_data_pri(self,RayosxCreate,extrainfo, **kwargs)

################################################
############# LISTAR DIAGNOSTICOS# #############
################################################

class ListDiagnostico(DetailView):
    model = Paciente
    template_name='registros/diagnostico_list.html'

################################################
#############  LISTAR ECOGRAFIAS   #############
################################################

class Listecoabdomen(DetailView):
    template_name='registros/listar_ecos/listar_ecoabdomen.html'
    model = Paciente
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parametro = self.kwargs.get('pk',None)
        analisis = analisisAbdominal.objects.filter(paciente__id=parametro)
        context['analisis']=analisis
        print(context)
        return context
    

class Listecoginecologo(DetailView):
    model = Paciente
    template_name='registros/listar_ecos/listar_ecoginecologia.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parametro = self.kwargs.get('pk',None)
        analisis = ecografiaginecologico.objects.filter(paciente__id=parametro)
        context['analisis']=analisis
        print(context)
        return context

class Listecomamas(DetailView):
    model = Paciente
    template_name='registros/listar_ecos/listar_ecomamas.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parametro = self.kwargs.get('pk',None)
        analisis = analisisMamas.objects.filter(paciente__id=parametro)
        context['analisis']=analisis
        print(context)
        return context

class Listecoobstetrico(DetailView):
    model = Paciente
    template_name='registros/listar_ecos/listar_ecoobstetrico.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parametro = self.kwargs.get('pk',None)
        analisis = analisisObstetrico.objects.filter(paciente__id=parametro)
        context['analisis']=analisis
        print(context)
        return context

class Listecorenal(DetailView):
    model = Paciente
    template_name='registros/listar_ecos/listar_ecorenal.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parametro = self.kwargs.get('pk',None)
        analisis = ecografiaRenal.objects.filter(paciente__id=parametro)
        context['analisis']=analisis
        print(context)
        return context

class Listecotesticular(DetailView):
    model = Paciente
    template_name='registros/listar_ecos/listar_ecotesticular.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parametro = self.kwargs.get('pk',None)
        analisis = ecografiatesticular.objects.filter(paciente__id=parametro)
        context['analisis']=analisis
        print(context)
        return context
