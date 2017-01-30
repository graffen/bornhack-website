# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-27 07:52


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20160712_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['available_in', 'price', 'name'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='ticket',
            name='checked_in',
            field=models.BooleanField(default=False),
        ),
    ]
