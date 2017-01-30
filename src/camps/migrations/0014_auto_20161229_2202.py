# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 22:02


import django.contrib.postgres.fields.ranges
from django.db import migrations
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0013_auto_20161229_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camp',
            name='buildup',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(help_text=b'The camp buildup period.', verbose_name=b'Buildup Period', default=(timezone.now(),None)),
        ),
        migrations.AlterField(
            model_name='camp',
            name='camp',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(help_text=b'The camp period.', verbose_name=b'Camp Period', default=(timezone.now(),None)),
        ),
        migrations.AlterField(
            model_name='camp',
            name='teardown',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(help_text=b'The camp teardown period.', verbose_name=b'Teardown period', default=(timezone.now(),None)),
        ),
    ]
