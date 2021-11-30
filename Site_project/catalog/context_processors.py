from django.core.handlers.wsgi import WSGIRequest

from catalog.models import Category


def nav_items_processor(request: WSGIRequest):
    categories = Category.objects.all()
    return {
        'nav_items': categories
    }
