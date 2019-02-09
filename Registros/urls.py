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
	path('ekg/<ident>', views.EkgCreate.as_view(),name='ekg'),
	path('terapias/<ident>', views.TerapiaCreate.as_view(),name='terapias'),
	path('rayosx/<ident>', views.RayosxCreate.as_view(),name='rayosx'),
	path('desintometria/<ident>', views.DesintometriaCreate.as_view(),name='desintometria'),

	path('ecomama/listar/<pk>', views.Listecomamas.as_view(),name='listar_ecomama'),
	path('ecoabdomen/listar/<pk>', views.Listecoabdomen.as_view(),name='listar_ecoabdomen'),
	path('ecoobstetrico/listar/<pk>', views.Listecoobstetrico.as_view(),name='listar_ecoobstetrico'),
	path('ecorenal/listar/<pk>', views.Listecorenal.as_view(),name='listar_ecorenal'),
	path('ecoginecologia/listar/<pk>', views.Listecoginecologo.as_view(),name='listar_ecoginecologia'),
	path('ecotesticular/listar/<pk>', views.Listecotesticular.as_view(),name='listar_ecotesticular'),

	path('paciente/listar_diagnostico/<pk>', views.ListDiagnostico.as_view(),name='lista_diagnostico'),
	path('paciente/nuevodiagnostico/<ident>', views.CreateOrderView.as_view(),name='nuevo_diagnostico'),

]