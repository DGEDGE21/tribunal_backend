# Generated by Django 3.0 on 2023-07-09 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0007_servicoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpedidos_quitacao',
            name='estado_info',
            field=models.CharField(default='processamento', max_length=1000),
        ),
        migrations.AddField(
            model_name='pedidos_quitacao',
            name='estado_info',
            field=models.CharField(default='processamento', max_length=1000),
        ),
    ]