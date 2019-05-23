# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-05-23 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='strategy',
            name='advisors',
        ),
        migrations.RemoveField(
            model_name='strategy',
            name='mgrnames',
        ),
        migrations.RemoveField(
            model_name='strategy',
            name='mscats',
        ),
        migrations.RemoveField(
            model_name='strategy',
            name='mssubadvs',
        ),
        migrations.RemoveField(
            model_name='strategy',
            name='user',
        ),
        migrations.RemoveField(
            model_name='strategyadvisor',
            name='Advisor',
        ),
        migrations.RemoveField(
            model_name='strategyadvisor',
            name='strategy',
        ),
        migrations.RemoveField(
            model_name='strategymgrname',
            name='MgrName',
        ),
        migrations.RemoveField(
            model_name='strategymgrname',
            name='strategy',
        ),
        migrations.RemoveField(
            model_name='strategymscat',
            name='MSCat',
        ),
        migrations.RemoveField(
            model_name='strategymscat',
            name='strategy',
        ),
        migrations.RemoveField(
            model_name='strategymssubadv',
            name='MSSubAdv',
        ),
        migrations.RemoveField(
            model_name='strategymssubadv',
            name='strategy',
        ),
        migrations.DeleteModel(
            name='Strategy',
        ),
        migrations.DeleteModel(
            name='StrategyAdvisor',
        ),
        migrations.DeleteModel(
            name='StrategyMgrName',
        ),
        migrations.DeleteModel(
            name='StrategyMSCat',
        ),
        migrations.DeleteModel(
            name='StrategyMSSubAdv',
        ),
    ]