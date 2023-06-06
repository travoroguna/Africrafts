from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('artisan-dashboard'), name='artisan-home'),
    path('dashboard', views.dashboard, name='artisan-dashboard'),
    path('products', views.products, name='artisan-products'),
    path('products/create', views.create_product, name='create-product'),
    path('products/edit/<int:product_id>', views.create_product, name='edit-product'),
    path('products/delete/<int:product_id>', views.delete_product, name='delete-product'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='all_login'),
    path('orders', views.orders, name='artisan_orders')
]
