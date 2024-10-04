# Generated by Django 5.1.1 on 2024-10-02 01:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("menu", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.client"
            ),
        ),
        migrations.AddField(
            model_name="orderdish",
            name="dish",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="menu.dish"
            ),
        ),
        migrations.AddField(
            model_name="orderdish",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="menu.order"
            ),
        ),
        migrations.AddField(
            model_name="schedule",
            name="menu",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="menu.menu"
            ),
        ),
    ]
