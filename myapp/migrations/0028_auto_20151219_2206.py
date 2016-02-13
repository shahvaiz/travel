# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_auto_20151219_2158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countryinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='countryinfo',
            name='iso_alpha2',
            field=models.CharField(default=1, max_length=2, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
