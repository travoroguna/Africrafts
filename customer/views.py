from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from customer.models import User, user_type


# Create your views here.
def shop(request):
    return render(request, 'customer_index.html')


def signup(request):
    if request.method != 'POST':
        return render(request, 'signup.html')
    
    email = request.POST.get('email')
    password = request.POST.get('password') 


    user = User.objects.create_user(email=email)
    user.set_password(password)
    user.save()

    user_type_obj = user_type(user=user, is_user=True)
    user_type_obj.save()


    return redirect('shop')
    

def login(request):
    if request.method != 'POST':
        return render(request, 'login.html')
    
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.get(email=email)

    if not user.check_password(password):
        return redirect('login')

    if user.user_type.is_user:
        return redirect('shop')
    elif user.user_type.is_artisan:
        return redirect('artisan:dashboard')
        