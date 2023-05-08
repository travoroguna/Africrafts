from django.shortcuts import redirect, render, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Customer
from artisan.models import Product


# Create your views here.


@login_required(login_url='/artisan/login', redirect_field_name=None)
def dashboard(request):
    if not request.user.is_artisan:
        return redirect('login')
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


def signup(request):
    if request.method != 'POST':
        return render(request, 'signup.html')
    
    email = request.POST.get('email')
    password = request.POST.get('password') 


    user = User.objects.create_user(email=email)
    user.set_password(password)
    user.save()

    user_type_obj = user_type(user=user, is_artisan=True)
    user_type_obj.save()

    artisan = User.objects.create_artisan(user=user)
    artisan.save()

    phone = request.POST.get('phone')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    zip_code = request.POST.get('zip_code')
    country = request.POST.get('country')
    description = request.POST.get('description')
    image = request.FILES.get('image')

    artisan_obj = Artisan(
        user=user,
        phone=phone,
        address=address,
        city=city,
        state=state,
        zip_code=zip_code,
        country=country,
        description=description,
        image=image
    )

    artisan_obj.save()

    return redirect('artisan:dashboard')
    

