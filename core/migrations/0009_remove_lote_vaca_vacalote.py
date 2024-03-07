# Generated by Django 5.0.2 on 2024-03-07 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_organizacao_lote_subdivisao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lote',
            name='vaca',
        ),
        migrations.CreateModel(
            name='VacaLote',
            fields=[
                ('id_vaca_lote', models.AutoField(primary_key=True, serialize=False)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('data_atualizacao', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('lote', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lote_vaca', to='core.lote')),
                ('vaca', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vaca_lote', to='core.animal')),
            ],
            options={
                'verbose_name': 'VacaLote',
                'verbose_name_plural': 'VacasLotes',
            },
        ),
    ]
