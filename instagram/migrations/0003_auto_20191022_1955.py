# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-22 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commenter',
            new_name='username',
        ),
    ]
