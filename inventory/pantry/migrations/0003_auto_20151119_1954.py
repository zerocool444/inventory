# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0002_auto_20151119_1953'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemType',
            new_name='ItemCategory',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_type',
            new_name='category',
        ),
    ]
