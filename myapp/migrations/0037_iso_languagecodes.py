# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_auto_20151225_0329'),
    ]

    operations = [
        migrations.CreateModel(
            name='iso_languagecodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso_639_3', models.CharField(max_length=4, null=True)),
                ('iso_639_2', models.CharField(max_length=50, null=True)),
                ('iso_639_1', models.CharField(max_length=50, null=True)),
                ('language_name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
