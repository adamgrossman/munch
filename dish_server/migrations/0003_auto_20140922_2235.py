# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish_server', '0002_auto_20140922_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'dish_photos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dish',
            name='price',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'member_photos', blank=True),
            preserve_default=True,
        ),
    ]
