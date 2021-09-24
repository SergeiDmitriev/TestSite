from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    slug = models.SlugField(max_length=32, unique=True, default='test')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    is_vegan = models.BooleanField(verbose_name="Вегатарианска?", default=False)
    slug = models.SlugField(max_length=32, unique=True, default='test')

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name="категория")
    modifier_groups = models.ManyToManyField('ModifierGroup', blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class ModifierGroup(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    slug = models.SlugField(max_length=32, unique=True, default='test')

    class Meta:
        verbose_name = 'Группа модификаторов'
        verbose_name_plural = 'Группы модификаторов'

    def __str__(self):
        return self.name


class Modifier(models.Model):
    name = models.CharField(max_length=32, verbose_name='Наименование')
    description = models.TextField(max_length=256, verbose_name='Описание')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    is_vegan = models.BooleanField(verbose_name="Вегатарианска?")
    slug = models.SlugField(max_length=32, unique=True, default='test')

    modifier_group = models.ForeignKey('ModifierGroup',
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       verbose_name='Группа модификаторов')

    class Meta:
        verbose_name = 'Модификатор'
        verbose_name_plural = 'Модификаторы'

    def __str__(self):
        return self.name
