from django.db import models


class Category_product(models.Model):
    name_category = models.CharField(primary_key=True, max_length=100)


class Name(models.Model):
    name_product = models.CharField(primary_key=True, max_length=250)
    nutrition_grade = models.CharField(default='E', max_length=1)
    picture_product = models.URLField(default='None')
    picture_nutrition = models.URLField(default='None')
    url_product = models.URLField(default='None')

