# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-08 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_stripe', '0006_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charges', to='pinax_stripe.Customer'),
        ),
    ]
