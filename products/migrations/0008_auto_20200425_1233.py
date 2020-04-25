# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-25 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200425_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_features',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_summary',
            field=models.TextField(default=''),
        ),
    ]
