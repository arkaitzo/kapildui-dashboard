# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20160321_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempDB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fuente', models.CharField(max_length=15)),
                ('fecha', models.DateTimeField(max_length=19)),
                ('tension', models.DecimalField(max_digits=5, decimal_places=3)),
            ],
        ),
    ]
