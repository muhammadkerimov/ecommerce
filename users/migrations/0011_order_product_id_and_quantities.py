# Generated by Django 4.2.7 on 2023-12-26 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_order_product_id_and_quantities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_id_and_quantities',
            field=models.JSONField(default=dict),
        ),
    ]
