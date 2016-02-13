# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20151219_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countryinfo',
            name='geoname',
            field=models.IntegerField(null=True),
        ),
    ]
