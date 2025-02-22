# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetId', models.BigIntegerField(default=0)),
                ('userId', models.BigIntegerField(default=0)),
                ('text', models.CharField(max_length=300)),
                ('createdAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.BigIntegerField(default=0)),
                ('handle', models.CharField(max_length=15)),
                ('displayName', models.CharField(max_length=20)),
            ],
        ),
    ]
