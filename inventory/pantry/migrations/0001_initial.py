# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Panty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expiration_date', models.DateField()),
                ('location', models.CharField(max_length=500, blank=True)),
                ('quantity', models.FloatField()),
                ('item', models.ForeignKey(to='pantry.Item')),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('short_code', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.ForeignKey(to='pantry.ItemType'),
        ),
        migrations.AddField(
            model_name='item',
            name='unit_of_measure',
            field=models.ForeignKey(to='pantry.UnitOfMeasure'),
        ),
    ]
