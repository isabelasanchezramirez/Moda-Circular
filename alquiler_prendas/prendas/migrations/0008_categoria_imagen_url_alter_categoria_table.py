# Generated by Django 5.1.2 on 2025-02-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prendas', '0007_alter_categoria_descripcion_alter_categoria_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagen_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterModelTable(
            name='categoria',
            table='categorias',
        ),
    ]
