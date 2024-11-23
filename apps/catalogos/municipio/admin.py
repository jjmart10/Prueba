from django.contrib import admin

from apps.catalogos.municipio.models import municipio

@admin.register(municipio)
class MunicipioAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['codigo', 'nombre']