# Generated by Django 5.0.4 on 2024-07-26 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppVentas', '0005_domicilio_numdomicilio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domicilio',
            name='numdomicilio',
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='iddomicilio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppVentas.domicilio', verbose_name='IDDomicilio'),
        ),
    ]
