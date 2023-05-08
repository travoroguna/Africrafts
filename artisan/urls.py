from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('artisan-dashboard'), name='artisan-home'),
    path('dashboard', views.dashboard, name='artisan-dashboard'),
    path('products', views.products, name='artisan-products'),
    path('products/create', views.create_product, name='create-product'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='all_login'),
]
