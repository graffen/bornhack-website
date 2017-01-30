# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 20:00


from django.conf import settings
import django.contrib.postgres.fields.jsonb
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('camps', '0004_camp_ticket_sale_open'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EpayCallback',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'verbose_name': 'Epay Callback',
                'verbose_name_plural': 'Epay Callbacks',
            },
        ),
        migrations.CreateModel(
            name='EpayPayment',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('txnid', models.IntegerField()),
                ('callback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.EpayCallback')),
            ],
            options={
                'verbose_name': 'Epay Payment',
                'verbose_name_plural': 'Epay Payments',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False, help_text='Whether this order has been paid.', verbose_name='Paid?')),
                ('payment_method', models.CharField(choices=[(b'credit_card', b'Credit card'), (b'altcoin', b'Altcoin'), (b'bank_transfer', b'Bank transfer')], default=b'credit_card', max_length=50)),
                ('camp', models.ForeignKey(help_text='The camp this order is for.', on_delete=django.db.models.deletion.CASCADE, to='camps.Camp', verbose_name='Camp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderProductRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField(help_text='Price of the ticket (in DKK).')),
                ('description', models.TextField()),
                ('available_in', django.contrib.postgres.fields.ranges.DateTimeRangeField(help_text='Which period is this ticket available for purchase? | (Format: YYYY-MM-DD HH:MM) | Only one of start/end is required')),
            ],
            options={
                'ordering': ['available_in'],
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.ProductCategory'),
        ),
        migrations.AddField(
            model_name='orderproductrelation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='shop.OrderProductRelation', to='shop.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(help_text='The user this order belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='epaypayment',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.Order'),
        ),
    ]
