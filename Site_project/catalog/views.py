from typing import Any

from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Count
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from cart.models import CartProduct
from catalog.models import Category, Product


class HomeView(View):
    def get(self, request):
        cat = Category.objects.all()
        return render(
            request,
            'catalog/home.html',
            {"categories": cat}
        )


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context: dict[str, Any] = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(Count('product'))
        return context


@login_required
def category_view(request: WSGIRequest, category_slug: str) -> HttpResponse:
    try:
        category: Category = (
            Category.objects
            .prefetch_related("product_set")
            .get(slug=category_slug)
        )
    except Category.DoesNotExist:
        raise Http404
    return render(
        request,
        'catalog/categories.html',
        {"category": category}
    )


@login_required
def product_view(request: WSGIRequest, product_slug: str) -> HttpResponse:
    try:
        product = (
            Product.objects
            .prefetch_related('productimage_set')
            .filter(slug=product_slug)
            .first()
        )
        is_in_cart = CartProduct.objects.filter(
            product=product,
            cart__user=request.user,
            cart__active=True).first()

        context = {
            'product': product,
            'is_in_cart': is_in_cart,
        }
    except Product.DoesNotExist:
        raise Http404
    return render(
        request,
        'catalog/product.html',
        context
    )

