# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FactorerMain', '0004_task_thread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='job_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='number_to_factor',
            field=models.CharField(max_length=200),
        ),
    ]
