from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import Customer
from artisan.models import Product

# Create your views here.


@login_required()
def dashboard(request):
    context = {
        'segment': 'dashboard',
        'customers': Customer.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'artisan_dashboard.html', context)
