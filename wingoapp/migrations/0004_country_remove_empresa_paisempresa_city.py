# Generated by Django 4.1.6 on 2023-02-27 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wingoapp', '0003_contacto_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('idPais', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del pais')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='paisEmpresa',
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('idEstado', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del estado')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wingoapp.country')),
            ],
        ),
    ]