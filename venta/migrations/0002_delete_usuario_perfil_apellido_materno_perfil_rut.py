# Generated by Django 4.2.1 on 2023-07-07 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='perfil',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='perfil',
            name='rut',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]