# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_remove_category_dummy_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]