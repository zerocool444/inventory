from django.db import models


class ItemCategory(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name


class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=500)
    short_code = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return ('%s (%s)' % (self.short_code, self.name,))


class Item(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(ItemCategory)
    unit_of_measure = models.ForeignKey(UnitOfMeasure)

    def __str__(self):
        return self.name

class Pantry(models.Model):
    item = models.ForeignKey(Item)
    expiration_date = models.DateField()
    location = models.CharField(max_length=500, blank=True)
    quantity = models.FloatField()

    def __str__(self):
        return self.item
