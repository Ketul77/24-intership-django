# Generated by Django 5.0.2 on 2024-03-05 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_developer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_manager',
        ),
    ]