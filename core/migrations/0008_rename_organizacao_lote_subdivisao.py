# Generated by Django 5.0.2 on 2024-03-07 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_animal_active_categoriaregistro_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lote',
            old_name='organizacao',
            new_name='subdivisao',
        ),
    ]