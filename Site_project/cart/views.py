from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from catalog.views import HomeView
from .models import Cart, CartProduct, Order, Customer
from catalog.models import Product


@login_required
def add(request, product_slug):
    slug_product = Product.objects.get(slug=product_slug)
    new_cart, _ = Cart.objects.get_or_create(user=request.user, is_active=True)
    new_product, _ = CartProduct.objects.get_or_create(product=slug_product, cart=new_cart)
    return redirect(reverse('catalog:home'))


@login_required
def cart(request):
    user = request.user
    customer, _ = Customer.objects.get_or_create(user=user)
    customer.save()
    cart_id = Cart.objects.filter(user_id=user.id).first()
    cart_products = CartProduct.objects.select_related('product').filter(cart_id=cart_id)
    full_price = total_sum(cart_products)
    if not cart:
        return redirect(reverse('catalog:home'))
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
def change_quantity(request, product_id):
    cart_product = CartProduct.objects.get(id=product_id)
    quantity_from_html = int(request.POST.get('quantity'))
    if quantity_from_html <= cart_product.product.quantity:
        cart_product.quantity = quantity_from_html
        cart_product.save()
    return redirect(reverse('cart:cart'))
