from django.urls import path
from . import views
from .views import paciente_new
app_name='registros'

urlpatterns = [
	path('', views.IndexView.as_view(),name='index'),
	path('busqueda/<nom>', views.BuscarView.as_view(),name='buscar'),
	path('paciente/<ident>', views.IngresoView.as_view(),name='paciente'),
	path('ecografia/<ident>', views.EcoView.as_view(),name='ecografia'),
	path('ecomama/<ident>', views.EcomamaCreate.as_view(),name='ecomama'),
	path('ecoabdomen/<ident>', views.EcoabdomenCreate.as_view(),name='ecoabdomen'),
	path('ecoobstetrico/<ident>', views.EcoobstetricoCreate.as_view(),name='ecoobstetrico'),
	path('ecorenal/<ident>', views.EcorenalCreate.as_view(),name='ecorenal'),
	path('ecoginecologia/<ident>', views.EcoginecologiaCreate.as_view(),name='ecoginecologia'),
	path('ecotesticular/<ident>', views.EcotesticularCreate.as_view(),name='ecotesticular'),
	path('pacienteini/',views.get_info,name='pat'),
	path('publishers/', paciente_new.as_view()),
	path('diagnostico/<paciente>/',paciente_new.as_view()),
	path('buscar/',views.BusquedaView.as_view()),
	path('buscar_ajax/',views.BusquedaAjaxView.as_view()),
]