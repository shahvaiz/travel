# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_auto_20151225_0313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternatename',
            old_name='alternatenameId',
            new_name='alternatenameid',
        ),
        migrations.AddField(
            model_name='alternatename',
            name='alternatename',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='alternatename',
            name='ispreferredname',
            field=models.NullBooleanField(),
        ),
    ]
