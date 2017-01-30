# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 16:45


import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0008_delete_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='camp',
            old_name='end',
            new_name='camp_end',
        ),
        migrations.RenameField(
            model_name='camp',
            old_name='start',
            new_name='camp_start',
        ),
        migrations.AddField(
            model_name='camp',
            name='buildup_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 20, 16, 45, 39, 609630, tzinfo=utc), help_text=b'When the camp buildup starts.', verbose_name=b'Buildup Start date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='camp',
            name='teardown_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 20, 16, 45, 44, 532143, tzinfo=utc), help_text=b'When the camp teardown ends.', verbose_name=b'Start date'),
            preserve_default=False,
        ),
    ]
