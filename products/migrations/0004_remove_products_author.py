# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-31 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='author',
        ),
    ]
