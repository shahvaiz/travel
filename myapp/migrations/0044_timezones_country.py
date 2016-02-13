# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0043_auto_20151227_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='timezones',
            name='country',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
