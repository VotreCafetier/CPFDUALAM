from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    products = Product.objects.all()
    color = Color.objects.all()
    context = {'products':products, 'colors':color}
    return render(request, 'index.html', context)