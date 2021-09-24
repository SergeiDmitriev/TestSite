from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def category_view(request, category_id):
        cat = Category.objects.prefetch_related("product_set").filter(id=category_id).first()
        return render(
            request,
            'catalog/product.html',
            {"category": cat}
        )
