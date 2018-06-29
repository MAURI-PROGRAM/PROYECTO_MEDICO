from django.urls import path
from . import views

urlpatterns = [
	path('', views.index,name='index'),
	path('<int:id_p>', views.detail,name='detalles'),
]
