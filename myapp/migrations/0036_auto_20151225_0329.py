# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_auto_20151225_0322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternatename',
            old_name='iscolloquialname',
            new_name='iscolloquial',
        ),
        migrations.RenameField(
            model_name='alternatename',
            old_name='ishistoricname',
            new_name='ishistoric',
        ),
    ]
