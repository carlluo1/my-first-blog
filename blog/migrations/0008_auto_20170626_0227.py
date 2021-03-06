# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-26 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170626_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='academic_subject',
            field=models.CharField(help_text='e.x Physics, Biology', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='phone_number',
            field=models.CharField(help_text='e.x 111-111-1111', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(help_text='e.x $3.00', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='year',
            field=models.CharField(help_text='e.x 1999', max_length=255, null=True),
        ),
    ]
