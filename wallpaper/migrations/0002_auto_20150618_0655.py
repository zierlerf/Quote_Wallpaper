# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='font',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='font',
            name='path',
            field=models.CharField(unique=True, max_length=500),
        ),
    ]
