# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_alternatename_geonameid'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryinfo',
            name='areainsqkm',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='capital',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='fips_code',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
