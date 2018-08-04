from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse
from .models import Paciente





class IndexView(generic.ListView):
	template_name='registros/index.html'
	context_object_name='all_albums'
	def get_queryset(self):
		return Paciente.objects.all()

class DetailView(generic.DetailView):
	model=Paciente
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