# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-04 17:12


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_eventtype_light_writing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventtype',
            old_name='light_writing',
            new_name='light_text',
        ),
    ]
