# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0011_prefijo_completo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefijo',
            name='completo',
            field=models.BigIntegerField(default=0),
        ),
    ]
