# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0041_featurecodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='timezones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeZoneId', models.CharField(max_length=200, null=True)),
                ('GMT_offset', models.DecimalField(max_digits=3, decimal_places=1)),
                ('DST_offset', models.DecimalField(max_digits=3, decimal_places=1)),
                ('raw_offset', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
        ),
    ]
