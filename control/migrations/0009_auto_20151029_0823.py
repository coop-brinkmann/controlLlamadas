# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0008_auto_20151029_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamada',
            name='corredor',
            field=models.CharField(default=b'NA', max_length=2, choices=[(b'TE', b'Telecom'), (b'CO', b'Colsecor'), (b'NA', b'No Aplica')]),
        ),
    ]
