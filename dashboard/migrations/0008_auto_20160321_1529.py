# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20160321_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempdb',
            name='valor',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
    ]
