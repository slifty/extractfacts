# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speak',
            fields=[
                ('claim', models.TextField(blank=True, null=True)),
                ('speaker', models.TextField(blank=True, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('trans_id', models.TextField(blank=True, null=True)),
                ('claim_id', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'speak',
                'managed': False,
            },
        ),
    ]