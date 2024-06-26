# Generated by Django 5.0.2 on 2024-04-04 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("address", models.CharField(max_length=200)),
                ("phone", models.IntegerField(max_length=10)),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("Manager", "manager"),
                            ("Sales", "sales"),
                            ("Software Developer", "sd"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.company"
                    ),
                ),
            ],
        ),
    ]
