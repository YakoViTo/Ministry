# Generated by Django 4.2.4 on 2023-09-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageWorkers', '0010_rename_nombre_afiliado_primer_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afiliado',
            name='primer_apellido',
            field=models.CharField(max_length=20, verbose_name='Primer Apellido'),
        ),
    ]
