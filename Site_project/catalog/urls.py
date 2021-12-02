from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('category/<slug:category_slug>/', views.category_view, name='category_view'),
    path('product/<slug:product_slug>/', views.product_view, name='product_view')
]
