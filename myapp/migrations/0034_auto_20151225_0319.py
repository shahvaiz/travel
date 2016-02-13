# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_auto_20151225_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternatename',
            name='iscolloquialname',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='alternatename',
            name='ishistoricname',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='alternatename',
            name='isshortname',
            field=models.NullBooleanField(),
        ),
    ]
