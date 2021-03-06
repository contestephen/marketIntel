# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basisFutures',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=20)),
                ('tradedate', models.DateTimeField(verbose_name='Trade Date')),
                ('month', models.CharField(max_length=10)),
                ('Open', models.TextField(max_length=5)),
                ('high', models.TextField(max_length=5)),
                ('low', models.TextField(max_length=5)),
                ('settle', models.TextField(max_length=5)),
                ('volume', models.CommaSeparatedIntegerField(max_length=20)),
                ('openInterest', models.CommaSeparatedIntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='gasFutures',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=20)),
                ('tradedate', models.DateTimeField(verbose_name='Trade Date')),
                ('month', models.CharField(max_length=10)),
                ('Open', models.TextField(max_length=5)),
                ('high', models.TextField(max_length=5)),
                ('low', models.TextField(max_length=5)),
                ('settle', models.TextField(max_length=5)),
                ('volume', models.CommaSeparatedIntegerField(max_length=20)),
                ('openInterest', models.CommaSeparatedIntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='gasStorage',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('reportDate', models.DateTimeField(verbose_name='report date')),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
