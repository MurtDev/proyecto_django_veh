# Generated by Django 5.1.1 on 2024-09-30 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'permissions': [('visualizar_catalogo', 'Puede visualizar el catálogo de vehículos'), ('add_vehiculomodel', 'Puede agregar vehículos')]},
        ),
    ]
