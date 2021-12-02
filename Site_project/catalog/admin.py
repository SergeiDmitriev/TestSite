from django.contrib import admin

from . import models


class ProductImageInLine(admin.TabularInline):
    model = models.ProductImage
    max_num = 3
    extra = 0


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    inlines = [ProductImageInLine]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
