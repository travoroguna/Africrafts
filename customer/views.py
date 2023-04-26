from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def shop(request):
    return render(request, 'customer_index.html')
