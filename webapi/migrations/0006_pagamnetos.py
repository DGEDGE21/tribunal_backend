# Generated by Django 3.0 on 2023-07-09 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0005_auto_20230709_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamnetos',
            fields=[
                ('idPagamento', models.BigAutoField(primary_key=True, serialize=False)),
                ('valor', models.CharField(max_length=1000)),
                ('descricao', models.CharField(max_length=1000)),
                ('idEmpresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapi.Empresa')),
            ],
        ),
    ]
