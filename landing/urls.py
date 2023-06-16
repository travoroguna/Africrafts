from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about', views.about_us, name= 'about_us')
]
