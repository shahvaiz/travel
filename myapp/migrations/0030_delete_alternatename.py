# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_auto_20151219_2237'),
    ]

    operations = [
        migrations.DeleteModel(
            name='alternatename',
        ),
    ]
