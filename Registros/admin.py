from django.contrib import admin
from .models import Paciente,Diagnostico,farmacoterapia,analisisMamas,analisisAbdominal,analisisObstetrico,ecografiaRenal,ecografiaginecologico,ecografiatesticular
# Register your models here.


class PacienteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['cedula','foto']}),
        ('Nombres', {'fields': ['nombre1','nombre2','apellPadre','apellMadre'], 'classes': ['collapse']}),
        ('Contactos', {'fields': ['telefono','celular','correo','pariente','parentesco','telefono_pariente','celular_pariente'], 'classes': ['collapse']}),
        ('Demograficos', {'fields': ['direccion','fechNacimiento','lugarNacimiento','nacionalidad','grupoCultural','sexo','tipo_sangre','estadoCivil'], 'classes': ['collapse']}),
        ('Ocupacion', {'fields': ['instruccion','ocupacion','empresa','tipo_seguro'], 'classes': ['collapse']}),
    ]
    list_display = ('__str__','cedula','fech_creado','celular')
    list_filter = ['fech_creado']
    search_fields = ['nombre1','nombre2','apellPadre','apellMadre','cedula',]

class farmacoterapiaInline(admin.TabularInline):
    model = farmacoterapia
    extra = 1

class DiagnosticoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['paciente','temperatura','peso','evolucion','pulso','saturacion_oxigeno','talla','idx','exmenes','motivo']}),
    ]
    readonly_fields = ()
    inlines = [farmacoterapiaInline]
    # list_display = ('__str__','cedula','fech_creado','celular')
    # list_filter = ['fech_creado']
    # search_fields = ['nombre1','nombre2','apellPadre','apellMadre','cedula',]



admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Diagnostico, DiagnosticoAdmin)
admin.site.register(analisisMamas)
admin.site.register(analisisAbdominal)
admin.site.register(analisisObstetrico)
admin.site.register(ecografiaRenal)
admin.site.register(ecografiaginecologico)
admin.site.register(ecografiatesticular)