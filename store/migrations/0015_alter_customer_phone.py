# Generated by Django 5.0.2 on 2024-02-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_customer_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
