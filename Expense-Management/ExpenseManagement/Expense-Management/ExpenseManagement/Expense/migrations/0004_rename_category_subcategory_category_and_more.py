# Generated by Django 5.0.2 on 2024-02-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0003_alter_category_name_alter_subcategory_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='Category',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='expense',
            name='paymentmethod',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('creditCard', 'Credit Card')], max_length=100),
        ),
        migrations.AlterField(
            model_name='expense',
            name='status',
            field=models.CharField(choices=[('cleared', 'Cleared'), ('uncleared', 'Uncleared'), ('void', 'Void')], max_length=100),
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
        migrations.AlterModelTable(
            name='subcategory',
            table='subcategory',
        ),
    ]
