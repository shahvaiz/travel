# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20151206_0431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternatename',
            old_name='alternatenameid',
            new_name='alternatenameId',
        ),
    ]
