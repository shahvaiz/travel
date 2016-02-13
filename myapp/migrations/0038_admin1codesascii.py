# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_iso_languagecodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin1CodesAscii',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20, null=True)),
                ('name', models.TextField(null=True)),
                ('nameAscii', models.TextField(null=True)),
                ('geonameid', models.IntegerField(null=True)),
            ],
        ),
    ]
