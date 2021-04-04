# Generated by Django 3.1.7 on 2021-03-22 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purbeurre', '0006_auto_20210322_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_product',
            name='name_category',
            field=models.CharField(default='None', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='name',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purbeurre.category_product'),
        ),
    ]