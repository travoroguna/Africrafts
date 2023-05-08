from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop')
    # path('signup', views.signup, name='signup')
    
]
