from django.urls import path, include
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='home'),
    path('<slug:category_slug>/', views.category_view, name='category_view'),

]
