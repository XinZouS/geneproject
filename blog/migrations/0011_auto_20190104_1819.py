# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-04 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190104_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='MSSubAdvs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=730)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='MSSubAdvId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.MSSubAdvs'),
        ),
    ]
