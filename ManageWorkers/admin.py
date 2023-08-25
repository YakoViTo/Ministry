from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Afiliado
from import_export import resources

admin.site.site_header = "SNFPMEANZ"
admin.site.index_title = "Sistema de gestión de afiliados al Sindicato Nacional de Funcionarios Públicos del Ministerio de Educación"
admin.site.site_url = "https://www.snfpmeanz.com/"

class AfiliadoResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Aplicar limpieza a los datos en la fila antes de importarla
        row['nombre'] = row['nombre'].strip()
        row['cod_cargo'] = str(row['cod_cargo']).strip()
        row['profession'] = row['profession'].strip()
        row['municipio'] = row['municipio'].strip()
        row['cod_plantel'] = str(row['cod_plantel']).strip()
        row['empresa'] = row['empresa'].strip()

    class Meta:
        model = Afiliado

class AfiliadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id", "nombre", "cod_cargo", "profession", "municipio", "cod_plantel", "empresa", "cuota", "formatted_fecha")
    search_fields = ("id", "nombre", "cod_cargo", "profession", "municipio", "cod_plantel", "empresa", "cuota", "formatted_fecha")
    list_filter = ("profession", "municipio", "empresa")
    date_hierarchy = "fecha"
    resource_class = AfiliadoResource
    list_per_page = 50
    
    def formatted_fecha(self, obj):
        return obj.fecha.strftime('%d-%m-%Y %H:%M')
    formatted_fecha.short_description = 'Fecha de Ingreso'

admin.site.register(Afiliado, AfiliadoAdmin)
