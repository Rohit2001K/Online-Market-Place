# Generated by Django 5.0.6 on 2024-09-21 15:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0010_alter_product_short_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]