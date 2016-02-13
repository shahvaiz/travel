# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alternatename'),
    ]

    operations = [
        migrations.CreateModel(
            name='countryinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso_alpha2', models.CharField(max_length=2, null=True)),
                ('iso_alpha3', models.CharField(max_length=3, null=True)),
                ('iso_numeric', models.IntegerField(null=True)),
            ],
        ),
    ]
