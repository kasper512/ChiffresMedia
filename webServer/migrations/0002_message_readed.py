# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webServer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='Readed',
            field=models.BooleanField(default=False),
        ),
    ]
