from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Afiliado
from import_export import resources

class AfiliadoResource(resources.ModelResource):
    class Meta:
        model = Afiliado
        
class AfiliadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=("id", "nombre", "cod_cargo", "profession", "municipio", "cod_plantel", "empresa")
    search_fields=("id", "nombre", "cod_cargo", "profession", "municipio", "cod_plantel", "empresa")
    list_filter=("profession", "municipio", "empresa")
    resource_class = AfiliadoResource

admin.site.register(Afiliado, AfiliadoAdmin)