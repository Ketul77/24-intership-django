# Generated by Django 5.0.2 on 2024-02-21 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='categoryid',
        ),
    ]
