# Generated by Django 4.2.4 on 2023-09-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageWorkers', '0015_alter_afiliado_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afiliado',
            name='fecha_de_nacimiento',
            field=models.DateField(),
        ),
    ]
