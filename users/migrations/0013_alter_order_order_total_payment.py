# Generated by Django 4.2.7 on 2023-12-27 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_order_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_total_payment',
            field=models.FloatField(default=0),
        ),
    ]
