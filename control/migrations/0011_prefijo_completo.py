# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0010_auto_20151029_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='prefijo',
            name='completo',
            field=models.IntegerField(default=0),
        ),
    ]
