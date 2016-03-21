# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20160321_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tensionesreceptor',
            name='diezminutal',
        ),
        migrations.RemoveField(
            model_name='tensionesreceptor',
            name='hora',
        ),
    ]
