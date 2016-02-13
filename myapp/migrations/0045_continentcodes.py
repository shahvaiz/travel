# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0044_timezones_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='continentcodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=2, null=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('geonameid', models.IntegerField(null=True)),
            ],
        ),
    ]
