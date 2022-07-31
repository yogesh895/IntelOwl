# Generated by Django 3.2.14 on 2022-07-31 15:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0009_datamigration'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='playbooks_requested',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='job',
            name='playbooks_to_execute',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=128), blank=True, default=list, size=None),
        ),
    ]
