# Generated by Django 3.0 on 2023-07-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='Representante',
            field=models.CharField(default=23, max_length=1000),
            preserve_default=False,
        ),
    ]
