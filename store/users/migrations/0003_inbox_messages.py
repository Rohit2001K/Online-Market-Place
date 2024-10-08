# Generated by Django 5.0.6 on 2024-09-23 09:48

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='inbox_messages',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('reciver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inbox_msg', to='users.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
    ]
