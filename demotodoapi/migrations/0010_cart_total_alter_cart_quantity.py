# Generated by Django 4.1 on 2023-01-28 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demotodoapi", "0009_remove_cart_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="total",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="cart",
            name="quantity",
            field=models.IntegerField(default=0),
        ),
    ]
