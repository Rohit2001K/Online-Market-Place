# Generated by Django 5.0.6 on 2024-09-15 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='user/user.jpg', upload_to='user/'),
        ),
    ]
