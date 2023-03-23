# Generated by Django 4.1.6 on 2023-03-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wingoapp', '0008_country_city_empresa_city_empresa_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='city',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='country',
        ),
        migrations.AddField(
            model_name='empresa',
            name='estado',
            field=models.CharField(default='Jalisco', help_text='Seleccione el estado', max_length=50, verbose_name='Estado de la empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='pais',
            field=models.CharField(default='México', help_text='Seleccione el pais', max_length=50, verbose_name='Pais de la empresa'),
            preserve_default=False,
        ),
    ]
