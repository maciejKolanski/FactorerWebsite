# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('FactorerMain', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='job_date',
            field=models.DateField(default=datetime.datetime(2016, 3, 16, 13, 49, 56, 354571, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
