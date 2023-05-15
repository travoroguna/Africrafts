from django.shortcuts import redirect, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# from shop.models import Customer
from artisan.models import Product, Artisan
from customer.models import User, user_type
from .forms import LoginForm


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
    return render(request, 'products/index.html', context)


@login_required()
def create_product(request):
    context = {
        'segment': 'products',
    }
    if request.method == 'POST':
        user = Artisan.objects.get(user=request.user)


        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        Product.objects.create(user=user, name=name, description=description, price=price, image=image)
        return redirect('/artisan/products', context)
    return render(request, 'products/create.html', context)


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