# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_countryinfo_geonameid'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryinfo',
            name='continent',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='currencycode',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='currencyname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='equivfipscode',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='languages',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='neighbors',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='population',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='postalcode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='postalcoderegex',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='countryinfo',
            name='tld',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
