# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('day', models.CharField(max_length=255)),
                ('hightemp', models.CharField(max_length=255)),
                ('lowtemp', models.CharField(max_length=255)),
                ('wind', models.CharField(max_length=255)),
                ('rain', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
