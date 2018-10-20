from django.urls import path
from . import views
from .views import paciente_new
app_name='registros'

urlpatterns = [
	path('', views.IndexView.as_view(),name='index'),
	path('busqueda', views.BuscarView.as_view(),name='buscar'),
	path('paciente', views.IngresoView.as_view(),name='paciente'),
	path('ecografia', views.EcoView.as_view(),name='ecografia'),
	path('ecomama', views.EcomamaCreate.as_view(),name='ecomama'),
	path('ecoabdomen', views.EcoabdomenCreate.as_view(),name='ecoabdomen'),
	path('ecoobstetrico', views.EcoobstetricoCreate.as_view(),name='ecoobstetrico'),
	path('ecorenal', views.EcorenalCreate.as_view(),name='ecorenal'),
	path('ecoginecologia', views.EcoginecologiaCreate.as_view(),name='ecoginecologia'),
	path('ecotesticular', views.EcotesticularCreate.as_view(),name='ecotesticular'),
	# path('inicio', views.inicio,name='inicio'),
	# path('lista', views.lista,name='lista'),
	# path('<int:pk>', views.DetailView.as_view(),name='detalles'),
	# path('album/add/',views.PacienteCreate.as_view(),name='album-add'),
	# # path('album/add/',views.PacienteCreate.as_view(),name='album-add'),
	path('pacienteini/',views.get_info,name='pat'),
	path('publishers/', paciente_new.as_view()),
	path('diagnostico/<paciente>/',paciente_new.as_view()),
]