# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0045_continentcodes'),
    ]

    operations = [
        migrations.CreateModel(
            name='postalcodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('countrycode', models.CharField(max_length=2, null=True)),
                ('postalcode', models.CharField(max_length=20, null=True)),
                ('placename', models.CharField(max_length=180, null=True)),
                ('admin1name', models.CharField(max_length=100, null=True)),
                ('admin1code', models.CharField(max_length=20, null=True)),
                ('admin2name', models.CharField(max_length=100, null=True)),
                ('admin2code', models.CharField(max_length=20, null=True)),
                ('admin3name', models.CharField(max_length=100, null=True)),
                ('admin3code', models.CharField(max_length=20, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('accuracy', models.IntegerField(null=True)),
            ],
        ),
    ]
