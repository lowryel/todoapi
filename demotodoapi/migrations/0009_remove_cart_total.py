# Generated by Django 4.1 on 2023-01-28 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("demotodoapi", "0008_alter_product_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="total",
        ),
    ]
