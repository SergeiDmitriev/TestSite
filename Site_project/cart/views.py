from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from catalog.models import Product
from .models import Cart, CartProduct, Customer


@login_required
def add_to_cart(request: WSGIRequest, product_slug: str):
    product = Product.objects.get(slug=product_slug)

    customer, _ = Customer.objects.get_or_create(user=request.user)
    customer.save()

    new_cart, _ = Cart.objects.get_or_create(customer=customer, active=True)
    new_cart.save()

    CartProduct.objects.get_or_create(product=product, cart=new_cart)
    return redirect(reverse('catalog:home'))


@login_required
def cart(request: WSGIRequest):
    user = request.user

    customer, _ = Customer.objects.get_or_create(user=user)
    customer.save()

    cart = Cart.objects.filter(customer=customer).first()
    if not cart:
        return redirect(reverse('catalog:home'))

    cart_products = CartProduct.objects.select_related('product').filter(cart=cart)
    full_price = total_sum(cart_products)

    context = {'cart_products': cart_products,
               'full_price': full_price}
    return render(request, 'cart/cart.html', context)


def total_sum(cart_products):
    price = 0
    for product in cart_products:
        quantity = product.quantity
        price += product.product.price*quantity
    return round(price, 2)


@login_required
def change_quantity(request: WSGIRequest, product_id: int):
    cart_product = CartProduct.objects.get(id=product_id)
    quantity_from_html = int(request.POST.get('quantity'))
    if quantity_from_html <= cart_product.product.quantity:
        cart_product.quantity = quantity_from_html
        cart_product.save()
    return redirect(reverse('cart:cart'))
