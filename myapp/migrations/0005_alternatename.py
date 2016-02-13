# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_geoname'),
    ]

    operations = [
        migrations.CreateModel(
            name='alternatename',
            fields=[
                ('alternatenameId', models.AutoField(serialize=False, primary_key=True)),
                ('isoLanguage', models.CharField(max_length=7, null=True)),
                ('alternateName', models.CharField(max_length=200, null=True)),
                ('isPreferredName', models.NullBooleanField()),
                ('isShortName', models.NullBooleanField()),
                ('isColloquial', models.NullBooleanField()),
                ('isHistoric', models.NullBooleanField()),
                ('geonameid', models.ForeignKey(to='myapp.geoname')),
            ],
        ),
    ]
