from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from customer.models import User, user_type
from artisan.models import Artisan


# Create your views here.
def home(request):
    return render(request, 'artisan_index.html')


@login_required(login_url='/artisan/login', redirect_field_name=None)
def dashboard(request):
    if not request.user.is_artisan:
        return redirect('login')
    context = {
        'segment': 'dashboard'
    }
    return render(request, 'artisan_dashboard.html', context)


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
    

