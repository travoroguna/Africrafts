from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from artisan.models import Product


# Create your views here.
def shop(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shop_index.html', context)
