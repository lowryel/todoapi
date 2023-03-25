# Generated by Django 4.1 on 2023-01-30 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("demotodoapi", "0010_cart_total_alter_cart_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="total",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AlterField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
