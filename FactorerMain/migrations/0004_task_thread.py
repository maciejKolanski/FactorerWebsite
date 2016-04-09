# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactorerMain', '0003_auto_20160320_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='thread',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
