# Generated by Django 4.0.1 on 2022-03-04 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
