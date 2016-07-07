# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Llamada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora', models.DateTimeField()),
                ('tipo', models.CharField(max_length=2, choices=[(b'EN', b'Entrante'), (b'SA', b'Saliente')])),
                ('celular', models.BooleanField()),
                ('numero_a', models.CharField(max_length=30)),
                ('numero_b', models.CharField(max_length=30)),
                ('duracion', models.IntegerField()),
                ('clave', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prefijo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prefijo', models.CharField(max_length=11)),
                ('localidad', models.CharField(max_length=300)),
                ('modalidad', models.CharField(max_length=3, choices=[(b'BAS', b'Basica'), (b'MOV', b'Movil'), (b'ESP', b'Especial'), (b'INT', b'Internacional'), (b'MPP', b'MPP'), (b'NOG', b'No Geografico')])),
            ],
        ),
    ]
