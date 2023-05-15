from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    # path('signup', views.signup, name='signup'),
    path('add_to_cart/<slug:slug>', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug:slug>', views.remove_from_cart, name='remove_from_cart'),
    path('store_cart', views.store_cart, name='store_cart'),
]
