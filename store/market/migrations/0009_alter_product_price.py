# Generated by Django 5.0.6 on 2024-09-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
