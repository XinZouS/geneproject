# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-04 01:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190104_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='MSCatDbId',
        ),
        migrations.DeleteModel(
            name='MSCats',
        ),
    ]
