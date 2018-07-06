from django.contrib import admin
from .models import Paciente,Diagnostico,farmacoterapia,analisisMamas
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Diagnostico)
admin.site.register(farmacoterapia)
admin.site.register(analisisMamas)