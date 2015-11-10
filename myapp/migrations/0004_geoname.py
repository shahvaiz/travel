# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_delete_geoname'),
    ]

    operations = [
        migrations.CreateModel(
            name='geoname',
            fields=[
                ('geonameid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('asciiname', models.CharField(max_length=200, null=True)),
                ('alternatenames', models.TextField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('fclass', models.CharField(max_length=1, null=True)),
                ('fcode', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=2, null=True)),
                ('cc2', models.CharField(max_length=60, null=True)),
                ('admin1', models.CharField(max_length=20, null=True)),
                ('admin2', models.CharField(max_length=80, null=True)),
                ('admin3', models.CharField(max_length=20, null=True)),
                ('admin4', models.CharField(max_length=20, null=True)),
                ('population', models.BigIntegerField(null=True)),
                ('elevation', models.IntegerField(null=True)),
                ('gtopo30', models.IntegerField(null=True)),
                ('timezone', models.CharField(max_length=40, null=True)),
                ('moddate', models.DateField(null=True)),
            ],
        ),
    ]
