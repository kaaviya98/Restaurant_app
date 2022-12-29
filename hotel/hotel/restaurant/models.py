from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "menu"
        verbose_name_plural = "menus"

    def __str__(self):
        return self.name


WEEKDAYS = [
    (1, ("Monday")),
    (2, ("Tuesday")),
    (3, ("Wednesday")),
    (4, ("Thursday")),
    (5, ("Friday")),
    (6, ("Saturday")),
    (7, ("Sunday")),
]
STATUS = [
    ("Open", "Open"),
    ("Closed", "Closed"),
]


class Timing(models.Model):

    weekday = models.IntegerField(choices=WEEKDAYS, unique=True)
    hours = models.CharField(max_length=10, choices=STATUS, default="draft")
    from_hour = models.TimeField(null=True, blank=True)
    to_hour = models.TimeField(null=True, blank=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="restaurant_owner"
    )
    location = models.CharField(max_length=200, db_index=True)
    address = models.TextField(max_length=50)
    timings = models.ForeignKey(
        Timing,
        related_name="restaurant_timings",
        on_delete=models.CASCADE,
    )
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)
        index_together = (("id", "slug"),)

    def __str__(self):
        return self.name


FOOD_TYPES = [
    ("Vegan", "Vegan"),
    ("Veg", "Veg"),
    ("Non-veg", "Non-veg"),
]


class FoodItem(models.Model):
    item_name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(max_length=50, blank=True)
    food_type = models.CharField(
        max_length=10, choices=FOOD_TYPES, default="draft"
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="food_items"
    )
