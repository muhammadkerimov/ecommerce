# Generated by Django 4.2.7 on 2023-12-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_order_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='additional_notes',
            field=models.CharField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='order',
            name='admin_delivery',
            field=models.CharField(default='Waiting', max_length=4000),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_son',
            field=models.BooleanField(default=False),
        ),
    ]
