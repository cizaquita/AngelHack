# Generated by Django 2.1 on 2018-08-05 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donaciones', '0002_auto_20180804_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='grupo_sanguineo',
            field=models.CharField(choices=[('Positivo', 'Positivo'), ('Negativo', 'Negativo')], max_length=9),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='rh',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=3),
        ),
        migrations.AlterUniqueTogether(
            name='inventario',
            unique_together={('rh', 'grupo_sanguineo')},
        ),
    ]
