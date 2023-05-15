from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from customer.models import User, user_type



def signup(request):
    if request.method != 'POST':
        return render(request, 'signup_customer-tmp.html')
    
    # TODO: Add validation for email and password
    email = request.POST.get('email')
    password = request.POST.get('password') 
    repeat_password = request.POST.get('repeat_password')

    if password != repeat_password:
        return redirect('customer_signup', {'error': 'Passwords do not match'})

    if User.objects.filter(email=email).exists():
        return redirect('customer_signup', {'error': 'Email already exists'})
    
    user = User.objects.create_user(email=email)
    user.set_password(password)
    user.save()

    user_type_obj = user_type(user=user, is_user=True)
    user_type_obj.save()


    return redirect('shop')
    