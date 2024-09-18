# Generated by Django 5.0.6 on 2024-09-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_product_bill_and_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bill_and_box',
            field=models.CharField(blank=True, choices=[('Yes', 'Have either bill/box'), ('No', "I don't have bill or box")], default=None, max_length=50, null=True),
        ),
    ]