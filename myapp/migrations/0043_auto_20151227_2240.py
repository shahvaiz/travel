# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0042_timezones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timezones',
            old_name='DST_offset',
            new_name='dst_offset',
        ),
        migrations.RenameField(
            model_name='timezones',
            old_name='GMT_offset',
            new_name='gmt_offset',
        ),
        migrations.RenameField(
            model_name='timezones',
            old_name='timeZoneId',
            new_name='timezoneid',
        ),
    ]
