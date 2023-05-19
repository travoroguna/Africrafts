from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def landing(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request,'about_us.html')