# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactorerMain', '0005_auto_20160418_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='first_factor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='element',
            name='second_factor',
            field=models.CharField(max_length=200),
        ),
    ]
