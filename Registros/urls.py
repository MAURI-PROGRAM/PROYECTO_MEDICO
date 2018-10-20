from django.urls import path
from . import views
from .views import paciente_new
app_name='registros'

urlpatterns = [
	path('', views.IndexView.as_view(),name='index'),
	# path('inicio', views.inicio,name='inicio'),
	# path('lista', views.lista,name='lista'),
	# path('<int:pk>', views.DetailView.as_view(),name='detalles'),
	# path('album/add/',views.PacienteCreate.as_view(),name='album-add'),
	# # path('album/add/',views.PacienteCreate.as_view(),name='album-add'),
	path('pacienteini/',views.get_info,name='pat'),
	path('publishers/', paciente_new.as_view()),
	path('diagnostico/<paciente>/',paciente_new.as_view()),
]