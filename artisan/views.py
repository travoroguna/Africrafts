from django.shortcuts import render, redirect
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


@login_required()
def products(request):
    context = {
        'segment': 'products',
        'products': Product.objects.all()
    }
    return render(request, 'products/index.html', context)


@login_required()
def create_product(request):
    context = {
        'segment': 'products',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        Product.objects.create(name=name, description=description, price=price, image=image)
        return redirect('/artisan/products', context)
    return render(request, 'products/create.html', context)
