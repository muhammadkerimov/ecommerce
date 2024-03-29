# Generated by Django 4.2.7 on 2024-01-10 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminaccs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=255)),
                ('admin_surname', models.CharField(max_length=255)),
                ('admin_id', models.CharField(max_length=255)),
                ('admin_password', models.CharField(max_length=255)),
                ('admin_level', models.CharField(choices=[('Moderator', 'level0'), ('Admin Level 1', 'level1'), ('Admin Level 2', 'level2'), ('Admin Level 3', 'level3'), ('Admin General', 'level4'), ('Owner', 'level5')], max_length=40)),
                ('admin_login_last', models.DateTimeField()),
            ],
        ),
    ]
