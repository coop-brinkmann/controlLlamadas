# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_auto_20151021_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosImportantes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ultima_importacion', models.DateTimeField()),
            ],
        ),
    ]
