# Generated by Django 5.0.6 on 2024-09-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0019_alter_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
