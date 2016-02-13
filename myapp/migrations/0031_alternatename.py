# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_delete_alternatename'),
    ]

    operations = [
        migrations.CreateModel(
            name='alternatename',
            fields=[
                ('alternatenameId', models.AutoField(serialize=False, primary_key=True)),
                ('geonameid', models.IntegerField(null=True)),
                ('isoLanguage', models.CharField(max_length=7, null=True)),
            ],
        ),
    ]
