# Generated by Django 4.1 on 2023-01-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demotodoapi", "0005_todo_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=120, null=True)),
                ("price", models.IntegerField()),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("order_created", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ManyToManyField(blank=True, to="demotodoapi.product"),
                ),
            ],
        ),
    ]