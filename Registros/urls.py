from django.urls import path
from . import views

app_name='registros'

urlpatterns = [
	path('', views.IndexView.as_view(),name='index'),
	
	path('buscar/',views.BusquedaView.as_view(),name='buscar'),
	path('buscar_ajax/',views.BusquedaAjaxView.as_view(),name='buscarajax'),

	path('nuevopaciente/', views.Crear_paciente.as_view(),name='newpaciente'),

	path('paciente/<ident>', views.IngresoView.as_view(),name='paciente'),
	path('ecografia/<ident>', views.EcoView.as_view(),name='ecografia'),

	path('ecomama/<ident>', views.EcomamaCreate.as_view(),name='ecomama'),
	path('ecoabdomen/<ident>', views.EcoabdomenCreate.as_view(),name='ecoabdomen'),
	path('ecoobstetrico/<ident>', views.EcoobstetricoCreate.as_view(),name='ecoobstetrico'),
	path('ecorenal/<ident>', views.EcorenalCreate.as_view(),name='ecorenal'),
	path('ecoginecologia/<ident>', views.EcoginecologiaCreate.as_view(),name='ecoginecologia'),
	path('ecotesticular/<ident>', views.EcotesticularCreate.as_view(),name='ecotesticular'),



]