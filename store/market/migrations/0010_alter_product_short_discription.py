# Generated by Django 5.0.6 on 2024-09-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_discription',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]