from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Afiliado(models.Model):# Creación de la tabla con el nombre Afiliado
    # Campos de la tabla
    
    MUNICIPIO_CHOICES = [
        ('ANACO', 'ANACO'),
        ('ARAGUA', 'ARAGUA'),
        ('BOLIVAR', 'BOLIVAR'),
        ('BRUZUAL', 'BRUZUAL'),
        ('CAJIGAL', 'CAJIGAL'),
        ('CAPISTRANO', 'CAPISTRANO'),
        ('CARVAJAL', 'CARVAJAL'),
        ('FREITES', 'FREITES'),
        ('GUANIPA', 'GUANIPA'),
        ('GUANTA', 'GUANTA'),
        ('INDEPENDENCIA', 'INDEPENDENCIA'),
        ('LIBERTAD', 'LIBERTAD'),
        ('McGREGOR', 'McGREGOR'),
        ('MIRANDA', 'MIRANDA'),
        ('MONAGAS', 'MONAGAS'),
        ('PEÑALVER', 'PEÑALVER'),
        ('PIRITU', 'PIRITU'),
        ('S.RODRIGUEZ', 'S.RODRIGUEZ'),
        ('SOTILLO', 'SOTILLO'),
        ('STA ANA', 'STA ANA'),
        ('URBANEJA', 'URBANEJA'),
    ]
    
    id = models.CharField(primary_key=True, max_length=20, verbose_name="Cédula de Identidad")
    nombre=models.CharField(max_length=50, verbose_name="Apellidos y Nombres")
    cod_cargo=models.CharField(max_length=50,verbose_name="Cod_Cargo")
    profession=models.CharField(max_length=50, verbose_name="Profesión u Oficio")
    municipio=models.CharField(max_length=20, verbose_name="Municipio", choices=MUNICIPIO_CHOICES)
    cod_plantel=models.CharField(max_length=50,verbose_name="Cod_Plantel")
    empresa=models.CharField(max_length=50, verbose_name="Empresa u organismo donde trabaja")
    cuota = models.DecimalField(
        max_digits=8,  # Número máximo de dígitos en total (incluyendo los decimales)
        decimal_places=2,  # Número de decimales permitidos
        validators=[MinValueValidator(0.01)],  # Validador para valores mínimos
        verbose_name="Cuota"
    )
    fecha=models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        # Eliminar espacios en blanco alrededor de los campos de texto
        self.id = self.id.strip()
        self.nombre = self.nombre.strip()
        self.cod_cargo = self.cod_cargo.strip()
        self.profession = self.profession.strip()
        self.municipio = self.municipio.strip()
        self.cod_plantel = self.cod_plantel.strip()
        self.empresa = self.empresa.strip()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name='afiliado'
        verbose_name_plural='afiliados'
        