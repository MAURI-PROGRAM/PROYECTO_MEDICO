from django.contrib import admin
from .models import Paciente,Diagnostico,farmacoterapia,analisisMamas,analisisAbdominal,analisisObstetrico
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Diagnostico)
admin.site.register(farmacoterapia)
admin.site.register(analisisMamas)
admin.site.register(analisisAbdominal)
admin.site.register(analisisObstetrico)