from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# from shop.models import Customer
from artisan.models import Product, Artisan
from customer.models import User, user_type
from .forms import LoginForm, ProductForm
from django.http import JsonResponse
from django.db.models import Q
from shop.models import OrderProduct


# Create your views here.


@login_required()
def dashboard(request):
    if not request.user.is_artisan:
        return redirect('login')
    context = {
        'segment': 'dashboard',
        'customers': [],
        'products': Product.objects.all()
    }
    return render(request, 'artisan_dashboard.html', context)


@login_required()
def products(request):
    context = {
        'segment': 'products',
        'products': Product.objects.filter(user=Artisan.objects.get(user=request.user)).all()
    }

    print(context['products'])
    return render(request, 'products/index.html', context)


@login_required()
def create_product(request, product_id=None):
    if product_id:
        # Edit an existing product
        product = get_object_or_404(Product, id=product_id)
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    else:
        # Create a new product
        form = ProductForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        context = {'segment': 'products'}
        if form.is_valid():
            if product_id is None:
                product = form.save(commit=False)
                product.user = Artisan.objects.get(user=request.user)
                product.save()
            else:
                form.save()
            return redirect('/artisan/products', context)
        else:
            context = {'form': form}
            return render(request, 'products/create.html', context)

    context = {'form': form, 'segment': 'products'}
    return render(request, 'products/create.html', context)


@login_required()
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return JsonResponse({'message': 'Product deleted successfully'})


def signup(request):
    if request.method != 'POST':
        return render(request, 'signup-tmp.html')

    email = request.POST.get('email')
    password = request.POST.get('password')

    if User.objects.filter(email=email).exists():
        return render(request, 'signup-tmp.html', {"error": "user with the email already exists"})

    artisan = User.objects.create_artisan(email=email, password=password)
    artisan.save()

    description = request.POST.get('description')

    artisan_obj = Artisan(
        user=artisan,
        description=description
    )

    artisan_obj.save()
    return redirect('artisan-dashboard')


def login(request):
    if request.method != 'POST':
        return render(request, 'login_tmp.html')

    form = LoginForm(request.POST)
    if not form.is_valid():
        return render(request, 'login_tmp.html', {'form': form})

    email = request.POST.get('email')
    password = request.POST.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        if user.is_artisan:
            return redirect('artisan-dashboard')
        else:
            return redirect('shop')

    return render(request, 'login_tmp.html', {'form': form, 'error': 'Invalid credentials'})


@login_required()
def orders(request):
    if not request.user.is_artisan:
        return redirect('login')

    artisan = Artisan.objects.get(user=request.user)
    placed_orders = OrderProduct.objects.filter(Q(product__user=artisan, ordered=True))
    for order in placed_orders:
        order.total = order.product.price * order.quantity

    context = {
        'segment': 'orders',
        'orders': placed_orders
    }

    return render(request, 'orders/index.html', context)
