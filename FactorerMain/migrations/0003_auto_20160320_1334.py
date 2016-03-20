# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FactorerMain', '0002_task_job_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('login', models.CharField(primary_key=True, max_length=45, serialize=False)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userdata',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
