from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse
from .models import Paciente
from .forms import PacienteForm
from django.shortcuts import render

class IndexView(generic.ListView):
	template_name='registros/index.html'
	context_object_name='all_albums'
	def get_queryset(self):
		return Paciente.objects.all()

class DetailView(generic.DetailView):
	model=Paciente
	context_object_name='paciente'
	template_name='registros/detail.html'

class PacienteCreate(CreateView):
	model=Paciente
	fields='__all__'

class PacienteUpdate(UpdateView):
	model=Paciente
	fields=['cedula','nombre1']

# class PacienteDelete(DeleteView):
# 	model=Paciente
# 	success_url=reverse('registros:index')
# 	fields=['cedula','nombre1']

def inicio(request):
    context = {}
    return render(request, 'registros/inicio.html', context)

def lista(request):
    context = {}
    return render(request, 'registros/lista_pacientes.html', context)


def get_info(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
        	form = PacienteForm()
        	return render(request, 'registros/form1.html', {'form': form})
    else:
        form = PacienteForm()
    return render(request, 'registros/form1.html', {'form': form})