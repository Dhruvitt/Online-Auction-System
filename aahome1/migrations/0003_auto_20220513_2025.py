# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2022-05-13 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aahome1', '0002_auto_20190919_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(default='future', max_length=30),
        ),
    ]
