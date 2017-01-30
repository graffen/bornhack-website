# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-12 21:19


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_auto_20160712_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='customorder',
            name='customer',
            field=models.TextField(default='', help_text='The customer info for this order, use <br> for newlines'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customorder',
            name='text',
            field=models.TextField(help_text='The invoice text'),
        ),
    ]
