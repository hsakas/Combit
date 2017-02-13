# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_job_dummy_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='dummy_field',
        ),
        migrations.AddField(
            model_name='category',
            name='dummy_field',
            field=models.CharField(default='dummy', max_length=250),
            preserve_default=False,
        ),
    ]
