from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Afiliado
from import_export import resources
from django.utils.html import format_html
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

# Personalización del encabezado del sitio de administración
admin.site.site_header = format_html('<img src="/static/img/logo-m3.jpg" alt="Ícono"> SNFPMEANZ')
admin.site.site_title = "SNFPMEANZ"
admin.site.index_title = "Sistema de gestión de afiliados al Sindicato Nacional de Funcionarios Públicos del Ministerio de Educación"
admin.site.site_url = "https://www.snfpmeanz.com/"

# Definición de un recurso para importar y exportar datos
class AfiliadoResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Aplicar limpieza a los datos en la fila antes de importarla
        row['nombre'] = row['nombre'].strip()
        row['cod_cargo'] = str(row['cod_cargo']).strip()
        row['profession'] = row['profession'].strip()
        row['municipio'] = row['municipio'].strip()
        row['cod_plantel'] = str(row['cod_plantel']).strip()
        row['plantel'] = row['plantel'].strip()

    class Meta:
        model = Afiliado

# Configuración personalizada para el administrador
class AfiliadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ("id", "nombre", "cod_cargo", "profession", "municipio", "cod_plantel", "plantel", "cuota", "formatted_fecha")
    search_fields = ("id", "nombre", "cod_cargo", "profession", "municipio", "cod_plantel", "plantel", "cuota")
    list_filter = (
        ('profession', DropdownFilter),
        ('municipio', DropdownFilter),
        ('plantel', DropdownFilter),
    )
    date_hierarchy = "fecha"
    resource_class = AfiliadoResource
    list_per_page = 25
    
    def formatted_fecha(self, obj):
        return obj.fecha.strftime('%d-%m-%Y %H:%M')
    formatted_fecha.short_description = 'Fecha de Ingreso'
# Registrar el modelo Afiliado con la configuración personalizada en el sitio de administración
admin.site.register(Afiliado, AfiliadoAdmin)
