# Generated by Django 3.0 on 2023-08-30 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0018_empresa_atencedentes_data_submisao'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpedidos_quitacao',
            name='assinalado',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='pedidos_quitacao',
            name='assinalado',
            field=models.CharField(default='0', max_length=2),
        ),
    ]
