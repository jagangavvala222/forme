# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-06 08:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='PythonDocument',
        ),
    ]
