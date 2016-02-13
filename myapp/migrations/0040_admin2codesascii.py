# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_auto_20151227_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin2codesascii',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=80, null=True)),
                ('name', models.TextField(null=True)),
                ('nameascii', models.TextField(null=True)),
                ('geonameid', models.IntegerField(null=True)),
            ],
        ),
    ]
