# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0002_auto_20170926_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
