# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_auto_20151219_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countryinfo',
            old_name='geonameid',
            new_name='geoname',
        ),
    ]
