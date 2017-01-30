# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-29 11:22


import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_coinifyapiinvoice_coinifycallback'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinifycallback',
            name='headers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coinifycallback',
            name='valid',
            field=models.BooleanField(default=False),
        ),
    ]
