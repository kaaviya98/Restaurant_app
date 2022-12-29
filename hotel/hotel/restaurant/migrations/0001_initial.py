# Generated by Django 4.1.4 on 2022-12-29 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Menu",
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
                ("name", models.CharField(db_index=True, max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "menu",
                "verbose_name_plural": "menus",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Timing",
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
                (
                    "weekday",
                    models.IntegerField(
                        choices=[
                            (1, "Monday"),
                            (2, "Tuesday"),
                            (3, "Wednesday"),
                            (4, "Thursday"),
                            (5, "Friday"),
                            (6, "Saturday"),
                            (7, "Sunday"),
                        ],
                        unique=True,
                    ),
                ),
                (
                    "hours",
                    models.CharField(
                        choices=[("Open", "Open"), ("Closed", "Closed")],
                        default="draft",
                        max_length=10,
                    ),
                ),
                ("from_hour", models.TimeField(blank=True, null=True)),
                ("to_hour", models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="FoodItem",
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
                ("item_name", models.CharField(db_index=True, max_length=200)),
                ("slug", models.SlugField(max_length=200)),
                ("description", models.TextField(blank=True, max_length=50)),
                (
                    "food_type",
                    models.CharField(
                        choices=[
                            ("Vegan", "Vegan"),
                            ("Veg", "Veg"),
                            ("Non-veg", "Non-veg"),
                        ],
                        default="draft",
                        max_length=10,
                    ),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="food_items",
                        to="restaurant.menu",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
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
                ("name", models.CharField(db_index=True, max_length=200)),
                ("slug", models.SlugField(max_length=200)),
                ("location", models.CharField(db_index=True, max_length=200)),
                ("address", models.TextField(max_length=50)),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurant.menu",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="restaurant_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "timings",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="restaurant_timings",
                        to="restaurant.timing",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
                "index_together": {("id", "slug")},
            },
        ),
    ]