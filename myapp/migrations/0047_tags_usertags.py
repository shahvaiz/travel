# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0046_postalcodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='tags',
            fields=[
                ('tagid', models.AutoField(serialize=False, primary_key=True)),
                ('tagname', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='usertags',
            fields=[
                ('usertagid', models.AutoField(serialize=False, primary_key=True)),
                ('userid', models.IntegerField(null=True)),
                ('tagid', models.IntegerField(null=True)),
                ('geonameid', models.IntegerField(null=True)),
            ],
        ),
    ]
