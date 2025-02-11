# Generated by Django 5.1.1 on 2024-10-02 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0004_remove_dish_dish_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="dish_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dishes",
                to="menu.dishtype",
            ),
        ),
    ]
