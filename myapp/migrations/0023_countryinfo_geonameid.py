# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_remove_countryinfo_geonameid'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryinfo',
            name='geonameid',
            field=models.ForeignKey(default=3981608, to='myapp.geoname'),
            preserve_default=False,
        ),
    ]
