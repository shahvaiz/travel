# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_auto_20151225_0319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternatename',
            old_name='isoLanguage',
            new_name='isolanguage',
        ),
    ]
