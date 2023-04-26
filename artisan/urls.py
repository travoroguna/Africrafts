from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='artisan-home'),
    path('dashboard', views.dashboard, name='artisan-dashboard')
]
