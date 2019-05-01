# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-04-30 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_fitdefault'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubAdv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FundId', models.CharField(max_length=10, null=True)),
                ('Fund', models.CharField(max_length=100)),
                ('SubAdvisor', models.CharField(max_length=200, null=True)),
                ('SubAdvisorParent', models.CharField(max_length=200, null=True)),
                ('AdvisorParent', models.CharField(max_length=100, null=True)),
                ('SubAdvised', models.CharField(max_length=3, null=True)),
                ('AgrmStart', models.DateField(null=True)),
                ('AgrmEnd', models.DateField(null=True)),
                ('SubStart', models.DateField(null=True)),
                ('SubEnd', models.DateField(null=True)),
                ('SubAlloc', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('SubAUM', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('FundAUM', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('EffSub', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('SubSched3', models.CharField(max_length=150, null=True)),
                ('SubAdvisorId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.FitSubAdvisors')),
            ],
        ),
    ]
