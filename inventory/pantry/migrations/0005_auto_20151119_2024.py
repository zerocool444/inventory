# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def initial_data(apps, schema_editor):
    data = [
        { 'id': '1', 'name': 'Beverages ', 'description': ' coffee/tea, juice, soda' },
        { 'id': '2', 'name': 'Bread/Bakery ', 'description': ' sandwich loaves, dinner rolls, tortillas, bagels' },
        { 'id': '3', 'name': 'Canned/Jarred Goods ', 'description': ' vegetables, spaghetti sauce, ketchup' },
        { 'id': '4', 'name': 'Dairy ', 'description': ' cheeses, eggs, milk, yogurt, butter' },
        { 'id': '5', 'name': 'Dry/Baking Goods ', 'description': ' cereals, flour, sugar, pasta, mixes' },
        { 'id': '6', 'name': 'Frozen Foods ', 'description': ' waffles, vegetables, individual meals, ice cream' },
        { 'id': '7', 'name': 'Meat ', 'description': ' lunch meat, poultry, beef, pork' },
        { 'id': '8', 'name': 'Produce ', 'description': ' fruits, vegetables' },
        { 'id': '9', 'name': 'Cleaners ', 'description': ' all- purpose, laundry detergent, dishwashing liquid/detergent' },
        { 'id': '10', 'name': 'Paper Goods ', 'description': ' paper towels, toilet paper, aluminum foil, sandwich bags' },
        { 'id': '11', 'name': 'Personal Care ', 'description': ' shampoo, soap, hand soap, shaving cream' },
        { 'id': '12', 'name': 'Other ', 'description': ' baby items, pet items, batteries, greeting cards' },
    ]

    Model = apps.get_model("pantry", "ItemCategory")

    for datum in data:
        try:
            model_instance = Model.objects.get(pk=datum['id'])
        except Model.DoesNotExist:
            model_instance = Model()
            model_instance.id = datum['id']

        model_instance.name = datum['name']
        model_instance.description = datum['description']
        model_instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0004_auto_20151119_2007'),
    ]

    operations = [
        migrations.RunPython(initial_data)
    ]
