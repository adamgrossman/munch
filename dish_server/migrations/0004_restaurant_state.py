# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish_server', '0003_auto_20140922_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='state',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
