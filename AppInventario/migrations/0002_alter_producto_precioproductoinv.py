# Generated by Django 5.0.6 on 2024-07-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precioproductoinv',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precioproductoinv'),
        ),
    ]
