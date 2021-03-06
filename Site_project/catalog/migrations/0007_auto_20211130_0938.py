# Generated by Django 3.2.7 on 2021-11-30 09:38

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='modifier_groups',
        ),
        migrations.AddField(
            model_name='product',
            name='cart_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img', validators=[catalog.validators.image_resolution_check_cart], verbose_name='Изображение для таблицы'),
        ),
        migrations.DeleteModel(
            name='Modifier',
        ),
        migrations.DeleteModel(
            name='ModifierGroup',
        ),
    ]
