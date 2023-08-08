from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Afiliado(models.Model):# Creación de la tabla con el nombre Afiliado
    # Campos de la tabla
    id = models.CharField(primary_key=True, max_length=20, verbose_name="Cédula de Identidad")
    nombre=models.CharField(max_length=20, verbose_name="Apellidos y Nombres")
    cod_cargo=models.PositiveIntegerField(validators=[MinValueValidator(1)],verbose_name="Cod_Cargo")
    profession=models.CharField(max_length=50, verbose_name="Profesión u Oficio")
    municipio=models.CharField(max_length=20, verbose_name="Municipio")
    cod_plantel=models.PositiveIntegerField(validators=[MinValueValidator(1)],verbose_name="Cod_Plantel")
    empresa=models.CharField(max_length=50, verbose_name="Empresa u organismo donde trabaja")
    #estatus = models.CharField(max_length=30, default='Habilitado')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name='afiliado'
        verbose_name_plural='afiliados'