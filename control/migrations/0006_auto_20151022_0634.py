# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0005_datosimportantes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosimportantes',
            name='ultima_importacion',
        ),
        migrations.AddField(
            model_name='datosimportantes',
            name='ultima_importacion_ama',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 9, 34, 40, 222000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosimportantes',
            name='ultima_importacion_lama',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 9, 34, 50, 902000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datosimportantes',
            name='ultima_importacion_telco',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 22, 9, 34, 59, 634000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
