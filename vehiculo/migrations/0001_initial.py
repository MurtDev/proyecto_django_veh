# Generated by Django 5.1.1 on 2024-09-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
