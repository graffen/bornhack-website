# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-29 10:47


import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_ticket_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoinifyAPIInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('invoicejson', django.contrib.postgres.fields.jsonb.JSONField()),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CoinifyCallback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
