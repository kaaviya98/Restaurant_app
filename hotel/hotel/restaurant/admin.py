from django.contrib import admin
from .models import Menu, Timing, Restaurant, FoodItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Timing)
class TimingAdmin(admin.ModelAdmin):
    list_display = ["weekday"]


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ["item_name", "slug"]
    prepopulated_fields = {"slug": ("item_name",)}
