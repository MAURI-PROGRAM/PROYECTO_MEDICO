from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.views.generic import ListView,DetailView

from django.views import View

from django.http import HttpResponseRedirect

from django.urls import reverse
from .models import Paciente,Diagnostico
from .forms import PacienteForm
from django.shortcuts import render




from django.views.generic import TemplateView

class IndexView(generic.ListView):
	template_name='registros/index.html'
	context_object_name='all_albums'
	def get_queryset(self):
		return Paciente.objects.all()

# class DetailView(generic.DetailView):
# 	model=Paciente
# 	context_object_name='paciente'
# 	template_name='registros/detail.html'

# class PacienteCreate(CreateView):
# 	model=Paciente
# 	fields='__all__'

# class PacienteUpdate(UpdateView):
# 	model=Paciente
# 	fields=['cedula','nombre1']

# class PacienteDelete(DeleteView):
# 	model=Paciente
# 	success_url=reverse('registros:index')
# 	fields=['cedula','nombre1']

# def inicio(request):
#     context = {}
#     return render(request, 'registros/inicio.html', context)

# def lista(request):
#     context = {}
#     return render(request, 'registros/lista_pacientes.html', context)


def get_info(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
        	form = PacienteForm()
        	return render(request, 'registros/form1.html', {'form': form})
    else:
        form = PacienteForm()
    return render(request, 'registros/form1.html', {'form': form})


class Crear_paciente():
    form_class = PacienteForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})





class paciente_new(ListView):
    template_name = 'registros/diagnostivo_list.html'
    def get_queryset(self):
        self.paciente = get_object_or_404(Paciente, name=self.kwargs['paciente'])
        return Diagnostico.objects.filter(paciente=self.paciente)
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['book_list'] = Diagnostico.objects.all()
    #     return context
