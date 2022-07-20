from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Propietario, Departamento

class PropietarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'edad', 'nacionalidad')
    search_fields = ('nombre', 'edad')

admin.site.register(Propietario, PropietarioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('costo_departamento', 'num_cuartos', 'num_banios','valor_alicuota')
    raw_id_fields = ('propietario',)

admin.site.register(Departamento, DepartamentoAdmin)
