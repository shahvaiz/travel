# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_countryinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alternatename',
            name='geonameid',
        ),
    ]
