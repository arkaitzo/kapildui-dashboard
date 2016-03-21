# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_tempdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tempdb',
            old_name='fuente',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='tempdb',
            old_name='tension',
            new_name='valor',
        ),
    ]
