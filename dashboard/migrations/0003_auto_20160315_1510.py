# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_corrientesolenoide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corrientesolenoide',
            name='corriente',
            field=models.DecimalField(max_digits=5, decimal_places=3),
        ),
    ]
