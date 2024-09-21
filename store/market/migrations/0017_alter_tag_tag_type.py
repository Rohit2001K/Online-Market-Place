# Generated by Django 5.0.6 on 2024-09-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_alter_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag_type',
            field=models.CharField(blank=True, choices=[('mobiles', 'Mobiles'), ('smartphones', 'Smartphones'), ('laptop', 'Laptop'), ('electronics', 'Electronics'), ('computer', 'Computer'), ('fashion_and_clothes', 'Fashion and Clothes'), ('house', 'House'), ('rent', 'Rent'), ('car', 'Car'), ('bike', 'Bike')], default=None, max_length=20, null=True),
        ),
    ]
