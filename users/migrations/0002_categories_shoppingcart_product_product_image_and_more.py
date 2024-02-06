# Generated by Django 4.2.7 on 2023-12-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=400)),
                ('category_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='shoppingcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id_and_quantities', models.JSONField()),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=None, upload_to='../product'),
        ),
        migrations.AddField(
            model_name='review',
            name='review_id',
            field=models.CharField(default=None, max_length=4000),
        ),
        migrations.AddField(
            model_name='review',
            name='star_count',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ordered_products',
            field=models.JSONField(default=None),
        ),
    ]
