# Generated by Django 5.0.2 on 2024-02-21 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_catergory_alter_product_table_product_catergory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='catergory',
        ),
    ]