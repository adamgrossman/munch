# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dish_server', '0004_restaurant_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='course',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
