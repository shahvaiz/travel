# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20151219_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryinfo',
            name='geonameid',
            field=models.ForeignKey(default=999, to='myapp.geoname'),
            preserve_default=False,
        ),
    ]
