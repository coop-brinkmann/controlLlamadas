# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0009_auto_20151029_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamada',
            name='clave',
            field=models.IntegerField(default=0),
        ),
    ]
