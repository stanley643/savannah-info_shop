# Generated by Django 5.0.4 on 2024-05-08 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_alter_order_item_remove_order_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.CharField(max_length=100),
        ),
    ]