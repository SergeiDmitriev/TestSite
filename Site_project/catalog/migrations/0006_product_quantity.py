# Generated by Django 3.2.7 on 2021-11-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество на складе'),
        ),
    ]
