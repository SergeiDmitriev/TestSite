import os.path
import uuid

from django.db import models

from catalog.validators import image_resolution_check_cart


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    slug = models.SlugField(max_length=32, unique=True, default='test')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    is_vegan = models.BooleanField(verbose_name="Вегатарианска?", default=False)
    slug = models.SlugField(max_length=32, unique=True, default='test')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество на складе')

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="категория"
        )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


def get_file_path(instance, image_name: str):
    ext = image_name.split('.')[-1]
    new_name = f'{uuid.uuid4()}.{ext}'
    return os.path.join('products', new_name)


class ProductImage(models.Model):
    cart_image = models.ImageField(
        validators=[image_resolution_check_cart],
        upload_to=get_file_path,
        verbose_name="Изображение для таблицы",
        null=True,
        blank=True
    )
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'Изображение для {self.product.name}'
