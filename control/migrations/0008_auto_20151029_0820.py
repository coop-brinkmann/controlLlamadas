# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0007_llamada_corredor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llamada',
            name='corredor',
            field=models.CharField(default=b'', max_length=2, blank=True, choices=[(b'TE', b'Telecom'), (b'CO', b'Colsecor')]),
        ),
    ]
