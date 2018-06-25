from django.contrib import admin
from .models import Paciente
from .models import Diagnostico
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Diagnostico)
