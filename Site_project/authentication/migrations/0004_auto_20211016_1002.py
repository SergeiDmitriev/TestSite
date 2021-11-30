# Generated by Django 3.2.7 on 2021-10-16 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_user_test_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Аватарка'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]