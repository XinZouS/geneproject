# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=400)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='AdvisorID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Advisors'),
        ),
    ]
