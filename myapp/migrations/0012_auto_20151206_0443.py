# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20151206_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alternatename',
            name='geonameid',
        ),
        migrations.DeleteModel(
            name='alternatename',
        ),
    ]
