# Generated by Django 4.1 on 2022-12-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demotodoapi", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="task",
            field=models.CharField(max_length=120, unique=True),
        ),
    ]