# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0006_auto_20151022_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='llamada',
            name='corredor',
            field=models.CharField(default=b'TE', max_length=2, choices=[(b'TE', b'Telecom'), (b'CO', b'Colsecor')]),
        ),
    ]
