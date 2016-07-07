# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prefijo',
            name='prefijo',
        ),
        migrations.AddField(
            model_name='prefijo',
            name='bloque',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prefijo',
            name='caracteristica',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
