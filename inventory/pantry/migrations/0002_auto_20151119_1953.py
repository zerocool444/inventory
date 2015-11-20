# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pantry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expiration_date', models.DateField()),
                ('location', models.CharField(max_length=500, blank=True)),
                ('quantity', models.FloatField()),
                ('item', models.ForeignKey(to='pantry.Item')),
            ],
        ),
        migrations.RemoveField(
            model_name='panty',
            name='item',
        ),
        migrations.DeleteModel(
            name='Panty',
        ),
    ]
