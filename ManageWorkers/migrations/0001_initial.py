# Generated by Django 4.2.4 on 2023-08-18 23:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Cédula de Identidad')),
                ('nombre', models.CharField(max_length=50, verbose_name='Apellidos y Nombres')),
                ('cod_cargo', models.CharField(max_length=50, verbose_name='Cod_Cargo')),
                ('profession', models.CharField(max_length=50, verbose_name='Profesión u Oficio')),
                ('municipio', models.CharField(choices=[('ANACO', 'ANACO'), ('ARAGUA', 'ARAGUA'), ('BOLIVAR', 'BOLIVAR'), ('BRUZUAL', 'BRUZUAL'), ('CAJIGAL', 'CAJIGAL'), ('CAPISTRANO', 'CAPISTRANO'), ('CARVAJAL', 'CARVAJAL'), ('FREITES', 'FREITES'), ('GUANIPA', 'GUANIPA'), ('GUANTA', 'GUANTA'), ('INDEPENDENCIA', 'INDEPENDENCIA'), ('LIBERTAD', 'LIBERTAD'), ('McGREGOR', 'McGREGOR'), ('MIRANDA', 'MIRANDA'), ('MONAGAS', 'MONAGAS'), ('PEÑALVER', 'PEÑALVER'), ('PIRITU', 'PIRITU'), ('S.RODRIGUEZ', 'S.RODRIGUEZ'), ('SOTILLO', 'SOTILLO'), ('STA ANA', 'STA ANA'), ('URBANEJA', 'URBANEJA')], max_length=20, verbose_name='Municipio')),
                ('cod_plantel', models.CharField(max_length=50, verbose_name='Cod_Plantel')),
                ('empresa', models.CharField(max_length=50, verbose_name='Empresa u organismo donde trabaja')),
                ('cuota', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cuota')),
            ],
            options={
                'verbose_name': 'afiliado',
                'verbose_name_plural': 'afiliados',
            },
        ),
    ]
