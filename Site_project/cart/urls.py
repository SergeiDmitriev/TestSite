from django.urls import path

from . import views


app_name = 'cart'
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<slug:product_slug>/', views.add_to_cart, name='add_to_cart'),
    path('change_quantity/<int:product_id>/', views.change_quantity, name='change_quantity'),
]
