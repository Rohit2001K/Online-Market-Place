# Generated by Django 5.0.6 on 2024-09-18 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_product_ownership_type_alter_product_discription_and_more'),
        ('users', '0002_alter_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]