# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PotenciasTransmisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('canal', models.CharField(max_length=13, choices=[(b'spbtxpowkw', b'Canal H'), (b'spbtxpowdpvkw', b'Canal V')])),
                ('fecha', models.DateTimeField(max_length=19)),
                ('potencia', models.DecimalField(max_digits=6, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='Temperaturas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sensor', models.CharField(max_length=14, choices=[(b'drxtempifcal', b'DRX1 IP'), (b'drxtempdig', b'DRX1 DIG'), (b'drxtempana', b'DRX1 ANA'), (b'drx1tempifcal', b'DRX2 IP'), (b'drx1tempdig', b'DRX2 DIG'), (b'drx1tempana', b'DRX2 ANA'), (b'ecupt100temp_1', b'ECU Sala Radar')])),
                ('fecha', models.DateTimeField(max_length=19)),
                ('temperatura', models.DecimalField(max_digits=5, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='TensionesReceptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fuente', models.CharField(max_length=12, choices=[(b'drxpowpos5', b'DRX1 de +5.0V'), (b'drxpowpos33', b'DRX1 de +3.3V'), (b'drxpowneg5', b'DRX1 de -5.0V'), (b'drx1powpos5', b'DRX2 de +5.0V'), (b'drx1powpos33', b'DRX2 de +3.3V'), (b'drx1powneg5', b'DRX2 de -5.0V')])),
                ('fecha', models.DateTimeField(max_length=19)),
                ('tension', models.DecimalField(max_digits=5, decimal_places=3)),
            ],
        ),
    ]
