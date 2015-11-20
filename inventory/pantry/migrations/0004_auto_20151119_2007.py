# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def initial_data(apps, schema_editor):
    data = [
        { 'id': 1, 'name': 'teaspoon ', 'short_code': 'tsp' },
        { 'id': 2, 'name': 'tablespoon ', 'short_code': 'tbsp' },
        { 'id': 3, 'name': 'fluid ounce', 'short_code': 'fl oz' },
        { 'id': 4, 'name': 'gill ', 'short_code': '' },
        { 'id': 5, 'name': 'cup ', 'short_code': 'c' },
        { 'id': 6, 'name': 'pint ', 'short_code': 'fl pt' },
        { 'id': 7, 'name': 'quart ', 'short_code': 'fl qt' },
        { 'id': 8, 'name': 'gallon ', 'short_code': 'g' },
        { 'id': 9, 'name': 'milliliter', 'short_code': 'mL' },
        { 'id': 10, 'name': 'liter', 'short_code': 'L' },
        { 'id': 11, 'name': 'deciliter', 'short_code': 'DL' },
        { 'id': 12, 'name': 'pound ', 'short_code': 'lb' },
        { 'id': 13, 'name': 'ounce ', 'short_code': 'oz' },
        { 'id': 14, 'name': 'milligram', 'short_code': 'mg' },
        { 'id': 15, 'name': 'gram', 'short_code': 'g' },
        { 'id': 16, 'name': 'kilogram', 'short_code': 'lkg' },
        { 'id': 17, 'name': 'millimeter', 'short_code': 'mm' },
        { 'id': 18, 'name': 'centimeter', 'short_code': 'cm' },
        { 'id': 19, 'name': 'meter', 'short_code': 'mm' },
        { 'id': 20, 'name': 'inch ', 'short_code': 'in' },
    ]

    Model = apps.get_model("pantry", "UnitOfMeasure")

    for datum in data:
        try:
            model_instance = Model.objects.get(pk=datum['id'])
        except Model.DoesNotExist:
            model_instance = Model()
            model_instance.id = datum['id']

        model_instance.name = datum['name']
        model_instance.short_code = datum['short_code']
        model_instance.save()



class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0003_auto_20151119_1954'),
    ]

    operations = [
        migrations.RunPython(initial_data)
    ]
