# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-22 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_funds'),
    ]

    operations = [
        migrations.CreateModel(
            name='MgrNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='MgrNameId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.MgrNames'),
        ),
    ]
