from django.urls import path, include
from . import views
from django.contrib.auth.views import login,logout_then_login
from django.contrib.auth.decorators import login_required
app_name='registros'

urlpatterns = [
	
	path('', views.IndexView.as_view(),name='index'),

	path('pdf/',login_required(views.PDFPrueba.as_view()),name='pdf'),
	path('pdf/ecomamas/<ident>',login_required(views.info_ecomamas.as_view()),name='info_ecomamas'),


	path('buscar/',login_required(views.BusquedaView.as_view()),name='buscar'),
	path('buscar_ajax/',login_required(views.BusquedaAjaxView.as_view()),name='buscarajax'),

	path('accounts/login/',login,{'template_name':'registros/login.html'},name='login'),
	path('logout/',logout_then_login,name='logout'),

	path('nuevopaciente/', login_required(views.Crear_paciente.as_view()),name='newpaciente'),

	path('paciente/<ident>', login_required(views.IngresoView.as_view()),name='paciente'),
	path('ecografia/<ident>', login_required(views.EcoView.as_view()),name='ecografia'),

	path('ecomama/<ident>', login_required(views.EcomamaCreate.as_view()),name='ecomama'),
	path('ecoabdomen/<ident>', login_required(views.EcoabdomenCreate.as_view()),name='ecoabdomen'),
	path('ecoobstetrico/<ident>', login_required(views.EcoobstetricoCreate.as_view()),name='ecoobstetrico'),
	path('ecorenal/<ident>', login_required(views.EcorenalCreate.as_view()),name='ecorenal'),
	path('ecoginecologia/<ident>', login_required(views.EcoginecologiaCreate.as_view()),name='ecoginecologia'),
	path('ecotesticular/<ident>', login_required(views.EcotesticularCreate.as_view()),name='ecotesticular'),
	path('ekg/<ident>', login_required(views.EkgCreate.as_view()),name='ekg'),
	path('terapias/<ident>', login_required(views.TerapiaCreate.as_view()),name='terapias'),
	path('rayosx/<ident>',login_required(views.RayosxCreate.as_view()),name='rayosx'),
	path('desintometria/<ident>', login_required(views.DesintometriaCreate.as_view()),name='desintometria'),

	path('ecomama/listar/<pk>', login_required(views.Listecomamas.as_view()),name='listar_ecomama'),
	path('ecoabdomen/listar/<pk>', login_required(views.Listecoabdomen.as_view()),name='listar_ecoabdomen'),
	path('ecoobstetrico/listar/<pk>', login_required(views.Listecoobstetrico.as_view()),name='listar_ecoobstetrico'),
	path('ecorenal/listar/<pk>', login_required(views.Listecorenal.as_view()),name='listar_ecorenal'),
	path('ecoginecologia/listar/<pk>', login_required(views.Listecoginecologo.as_view()),name='listar_ecoginecologia'),
	path('ecotesticular/listar/<pk>',login_required(views.Listecotesticular.as_view()),name='listar_ecotesticular'),

	path('paciente/listar_diagnostico/<pk>', login_required(views.ListDiagnostico.as_view()),name='lista_diagnostico'),
	path('paciente/nuevodiagnostico/<ident>', login_required(views.CreateOrderView.as_view()),name='nuevo_diagnostico'),

]