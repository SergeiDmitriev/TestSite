from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

from catalog.models import Product


class Cart(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)


class CartProduct(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct')
    date = models.DateField(auto_now=True)
