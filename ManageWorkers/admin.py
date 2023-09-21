from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Afiliado
from import_export import resources
from django.utils.html import format_html
from datetime import datetime
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter

# Personalización del encabezado del sitio de administración
admin.site.site_header = format_html('<img src="/static/img/logo-m3.jpg" alt="Ícono"> SNFPMEANZ')
admin.site.site_title = "SNFPMEANZ"
admin.site.index_title = "Sistema de gestión de afiliados al Sindicato Nacional de Funcionarios Públicos del Ministerio de Educación"

# Definición de un recurso para importar y exportar datos
class AfiliadoResource(resources.ModelResource):
    def before_import_row(self, row, **kwargs):
        # Aplicar limpieza a los datos en la fila antes de importarla
        row['primer_apellido'] = row['primer_apellido'].strip()
        if row['segundo_apellido'] is not None:
            row['segundo_apellido'] = row['segundo_apellido'].strip()
        row['primer_nombre'] = row['primer_nombre'].strip()
        if row['segundo_nombre'] is not None:
            row['segundo_nombre'] = row['segundo_nombre'].strip()
        row['sexo'] = row['sexo'].strip()
        fecha = row['fecha_de_nacimiento']
        fechastr = str(fecha).strip()
        try:
            # Intenta analizar la fecha en varios formatos
            date_obj = datetime.strptime(fechastr, '%d/%m/%Y')
        except ValueError:
            try:
                date_obj = datetime.strptime(fechastr, '%Y-%m-%d')
                # Convierte la fecha al formato deseado
                row['fecha_de_nacimiento'] = date_obj.strftime('%d/%m/%Y')
            except ValueError:
                # Manejar otros formatos de fecha si es necesario
                pass
        row['cod_cargo'] = str(row['cod_cargo']).strip()
        row['profession'] = row['profession'].strip()
        row['municipio'] = row['municipio'].strip()
        row['cod_plantel'] = str(row['cod_plantel']).strip()
        row['plantel'] = row['plantel'].strip()
        row['cuota'] = str(row['cuota']).strip()

    class Meta:
        model = Afiliado

# Configuración personalizada para el administrador
class AfiliadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ("id", "primer_apellido", "segundo_apellido", "primer_nombre", "segundo_nombre", "sexo", "formatted_fecha", "cod_cargo", "profession", "municipio", "cod_plantel", "plantel", "cuota")
    search_fields = ("id", "primer_apellido", "segundo_apellido", "primer_nombre", "segundo_nombre", "sexo", "cod_cargo", "profession", "municipio", "cod_plantel", "plantel", "cuota")
    list_filter = (
        ('profession', ChoiceDropdownFilter),
        ('municipio', ChoiceDropdownFilter),
        ('plantel', ChoiceDropdownFilter),
    )
    date_hierarchy = "fecha_de_nacimiento"
    resource_class = AfiliadoResource
    list_per_page = 25
    
    def formatted_fecha(self, obj):
        return obj.fecha_de_nacimiento.strftime('%d/%m/%Y')
    formatted_fecha.short_description = 'Fecha de Nacimiento'
    
    def has_import_permission(self, request):
        # Limitar la importación al superusuario y usuarios con el permiso personalizado
        if request.user.is_superuser or request.user.has_perm('ManageWorkers.can_import_afiliado'):
            return True
        return False
    
    def has_export_permission(self, request):
        # Limitar la importación al superusuario y usuarios con el permiso personalizado
        if request.user.is_superuser or request.user.has_perm('ManageWorkers.can_export_afiliado'):
            return True
        return False
    
# Registrar el modelo Afiliado con la configuración personalizada en el sitio de administración
admin.site.register(Afiliado, AfiliadoAdmin)
