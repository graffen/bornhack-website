# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 22:23


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_auto_20160530_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
