# Generated by Django 3.1.7 on 2021-03-17 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_product',
            fields=[
                ('name_category', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('name_product', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('nutrition_grade', models.CharField(default='E', max_length=1)),
                ('picture_product', models.URLField(default='None')),
                ('picture_nutrition', models.URLField(default='None')),
                ('url_product', models.URLField(default='None')),
            ],
        ),
    ]
