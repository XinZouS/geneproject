# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-10 20:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_shares'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shares',
        ),
    ]