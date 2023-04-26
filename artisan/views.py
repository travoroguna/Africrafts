from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'artisan_index.html')


@login_required()
def dashboard(request):
    context = {
        'segment': 'dashboard'
    }
    return render(request, 'artisan_dashboard.html', context)
