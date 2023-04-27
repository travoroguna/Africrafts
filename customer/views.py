from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from customer.models import User, user_type


# Create your views here.
def shop(request):
    return render(request, 'customer_index.html')


def signup(request):
    if request.method != 'POST':
        return render(request, 'customer_signup.html')
    
    # TODO: Add validation for email and password
    email = request.POST.get('email')
    password = request.POST.get('password') 
    repeat_password = request.POST.get('repeat_password')

    if password != repeat_password:
        return redirect('signup', {'error': 'Passwords do not match'})


    user = User.objects.create_user(email=email)
    user.set_password(password)
    user.save()

    user_type_obj = user_type(user=user, is_user=True)
    user_type_obj.save()


    return redirect('shop')
    