# Generated by Django 5.0.2 on 2024-02-25 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]