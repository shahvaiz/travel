# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_tags_usertags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='tagname2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
