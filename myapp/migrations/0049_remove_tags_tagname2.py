# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_tags_tagname2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='tagname2',
        ),
    ]
