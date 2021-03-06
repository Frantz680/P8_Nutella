# Generated by Django 3.1.7 on 2021-03-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_product',
            fields=[
                ('id', models.AutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(
                    default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('name_product', models.CharField(max_length=250,
                                                  unique=True)),
                ('nutrition_grade', models.CharField(default='E',
                                                     max_length=1)),
                ('picture_product', models.URLField(default='None')),
                ('picture_nutrition', models.URLField(default='None')),
                ('url_product', models.URLField(default='None')),
                ('category', models.ForeignKey(
                    default='None',
                    on_delete=django.db.models.deletion.CASCADE,
                    to='purbeurre.category_product')),
            ],
        ),
    ]
