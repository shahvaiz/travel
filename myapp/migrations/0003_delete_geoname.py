# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_abc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='geoname',
        ),
    ]
