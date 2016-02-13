# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_admin1codesascii'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin1codesascii',
            old_name='nameAscii',
            new_name='nameascii',
        ),
    ]
