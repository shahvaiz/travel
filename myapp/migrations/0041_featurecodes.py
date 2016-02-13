# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_admin2codesascii'),
    ]

    operations = [
        migrations.CreateModel(
            name='featureCodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=7, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
