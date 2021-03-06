# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170623_0202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='additional_comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='book_name',
        ),
        migrations.AddField(
            model_name='post',
            name='academic_subject',
            field=models.CharField(default='e.x Physics, Biology', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default='e.x fakeemail@gmail.com', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(default='SAT, ACT, Workbook, etc.', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='phone_number',
            field=models.CharField(default='e.x 111-111-1111', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.CharField(default='e.x $3.00', max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='year',
            field=models.CharField(default='e.x 1999', max_length=255),
        ),
    ]
