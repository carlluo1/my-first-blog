# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170627_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(blank=True, choices=[('d', 'N/A'), ('a', 'ACT Test Prep'), ('b', 'Study Guide'), ('c', 'AP Test Prep'), ('e', 'SAT Test Prep'), ('f', 'SAT Test Prep'), ('g', 'Textbook'), ('h', 'Workbook')], default='d', help_text='Select a Genre, do not leave blank', max_length=1),
        ),
    ]
