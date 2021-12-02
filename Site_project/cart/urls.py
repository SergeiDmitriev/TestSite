from django.contrib.auth import get_user_model
from django.urls import path
from . import views


app_name = 'cart'
urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<slug:product_slug>/', views.add, name='add'),
    path('change_quantity/<int:product_id>/', views.change_quantity, name='change_quantity'),
]