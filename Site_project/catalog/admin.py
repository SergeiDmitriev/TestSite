from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Modifier)
class ModifierAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ModifierGroup)
class ModifierGroupAdmin(admin.ModelAdmin):
    pass
