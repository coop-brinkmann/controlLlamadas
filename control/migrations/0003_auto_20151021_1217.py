# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_auto_20151021_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefijo',
            name='bloque',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='prefijo',
            name='caracteristica',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AlterField(
            model_name='prefijo',
            name='localidad',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AlterField(
            model_name='prefijo',
            name='modalidad',
            field=models.CharField(default=b'BAS', max_length=3, choices=[(b'BAS', b'Basica'), (b'MOV', b'Movil'), (b'ESP', b'Especial'), (b'INT', b'Internacional'), (b'MPP', b'MPP'), (b'NOG', b'No Geografico')]),
        ),
    ]
