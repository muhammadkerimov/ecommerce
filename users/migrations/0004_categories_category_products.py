# Generated by Django 4.2.7 on 2023-12-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_payment_receipt_alter_product_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='category_products',
            field=models.JSONField(default=[]),
        ),
    ]
