# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_to_factor', models.CharField(max_length=200)),
                ('job_date', models.DateField(default=django.utils.timezone.now)),
                ('state', models.IntegerField(default=0, choices=[(-1, b'Cancelled'), (0, b'Undone'), (1, b'Working'), (2, b'Done')])),
                ('priority', models.IntegerField(default=0)),
                ('result', models.CharField(max_length=300)),
                ('algorithm', models.ForeignKey(to='FactorerMain.Algorithm')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('login', models.CharField(max_length=45, serialize=False, primary_key=True)),
                ('mail', models.EmailField(max_length=254)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
