# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20160506_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(choices=[('credit_card', 'Credit card'), ('altcoin', 'Altcoin'), ('bank_transfer', 'Bank transfer')], default='credit_card', max_length=50),
        ),
    ]
