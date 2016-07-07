# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_auto_20151021_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamada',
            name='numero_a',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='llamada',
            name='numero_b',
            field=models.CharField(default=b'', max_length=30),
        ),
        migrations.AlterField(
            model_name='prefijo',
            name='bloque',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='prefijo',
            name='caracteristica',
            field=models.IntegerField(),
        ),
    ]
