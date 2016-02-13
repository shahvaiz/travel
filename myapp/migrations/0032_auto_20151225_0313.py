# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_alternatename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countryinfo',
            old_name='geoname',
            new_name='geonameid',
        ),
    ]
