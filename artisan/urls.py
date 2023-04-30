from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('artisan-dashboard'), name='artisan-home'),
    path('dashboard', views.dashboard, name='artisan-dashboard')
]
