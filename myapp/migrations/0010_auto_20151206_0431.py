# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20151206_0417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternatename',
            old_name='alternatenameId',
            new_name='alternatenameid',
        ),
    ]
