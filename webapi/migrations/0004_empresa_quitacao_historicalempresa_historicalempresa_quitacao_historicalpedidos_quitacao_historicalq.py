# Generated by Django 3.0 on 2023-07-08 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapi', '0003_empresa_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quitacao',
            fields=[
                ('idQuitacao', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_emissao', models.DateField(auto_now_add=True)),
                ('data_expiracao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos_Quitacao',
            fields=[
                ('idPedido', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_submisao', models.DateField(auto_now_add=True)),
                ('idEmpresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapi.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalQuitacao',
            fields=[
                ('idQuitacao', models.BigIntegerField(blank=True, db_index=True)),
                ('data_emissao', models.DateField(blank=True, editable=False)),
                ('data_expiracao', models.DateField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical quitacao',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPedidos_Quitacao',
            fields=[
                ('idPedido', models.BigIntegerField(blank=True, db_index=True)),
                ('data_submisao', models.DateField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('idEmpresa', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='webapi.Empresa')),
            ],
            options={
                'verbose_name': 'historical pedidos_ quitacao',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalEmpresa_Quitacao',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('idEmpresa', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='webapi.Empresa')),
                ('idQuitacao', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='webapi.Quitacao')),
            ],
            options={
                'verbose_name': 'historical empresa_ quitacao',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalEmpresa',
            fields=[
                ('idEmpresa', models.BigIntegerField(blank=True, db_index=True)),
                ('nome', models.CharField(max_length=1000)),
                ('nuit', models.CharField(max_length=1000)),
                ('endereco', models.CharField(max_length=1000)),
                ('vocacao', models.CharField(max_length=1000)),
                ('objectivo', models.CharField(max_length=1000)),
                ('Representante', models.CharField(max_length=1000)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical empresa',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Empresa_Quitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEmpresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapi.Empresa')),
                ('idQuitacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapi.Quitacao')),
            ],
        ),
    ]
