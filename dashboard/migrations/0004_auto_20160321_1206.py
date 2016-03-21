# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20160315_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='tensionesreceptor',
            name='diezminutal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tensionesreceptor',
            name='hora',
            field=models.IntegerField(default=0),
        ),
    ]
