# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('idTransaccion', models.AutoField(primary_key=True, serialize=False)),
                ('idVendedor', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'transacciones',
            },
        ),
    ]