# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-04-30 23:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_subadv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subadv',
            name='SubAdvisorId',
        ),
        migrations.DeleteModel(
            name='SubAdv',
        ),
    ]